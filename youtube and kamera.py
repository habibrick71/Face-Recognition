import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
from vidgear.gears import CamGear
import tkinter as tk
from tkinter import messagebox

def detect_objects_youtube(url):
    # Initialize the YouTube video stream
    stream = CamGear(source=url, stream_mode=True, logging=True).start()
    
    while True:
        # Read a frame from the YouTube video stream
        frame = stream.read()
        
        # Resize the frame
        frame = cv2.resize(frame, (1020, 600))
        
        # Detect objects in the frame
        bbox, label, conf = cv.detect_common_objects(frame)
        
        # Draw bounding boxes around the detected objects
        frame = draw_bbox(frame, bbox, label, conf)
        
        # Count the number of cars and persons
        c = label.count('car')
        p = label.count('person')
        
        # Display the counts on the frame
        cv2.putText(frame, str(c), (50, 60), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)
        cv2.putText(frame, str(p), (50, 80), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 3)
        
        # Display the frame
        cv2.imshow("FRAME", frame)
        
        # Exit on pressing the 'Esc' key
        if cv2.waitKey(1) & 0xFF == 27:
            break
    
    # Release the YouTube video stream and close all OpenCV windows
    stream.release()
    cv2.destroyAllWindows()

def detect_objects_webcam():
    # Initialize the webcam
    cap = cv2.VideoCapture(0)
    
    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()
        
        # Resize the frame
        frame = cv2.resize(frame, (1020, 600))
        
        # Detect objects in the frame
        bbox, label, conf = cv.detect_common_objects(frame)
        
        # Draw bounding boxes around the detected objects
        frame = draw_bbox(frame, bbox, label, conf)
        
        # Count the number of cars and persons
        c = label.count('car')
        p = label.count('person')
        
        # Display the counts on the frame
        cv2.putText(frame, str(c), (50, 60), cv2.FONT_HERSHEY_PLAIN, 3, (255, 255, 25))