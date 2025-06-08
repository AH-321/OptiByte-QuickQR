import os
import json
import time
from typing import List, Optional
import cv2
import numpy as np
from pyzbar.pyzbar import decode

def loadData(file_path: str) -> List[str]:
    """Load previously scanned data from JSON file."""
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def saveData(file_path: str, data: List[str]) -> None:
    """Save scanned data to JSON file."""
    with open(file_path, "w") as file:
        json.dump(data, file)


def processDecodedObjects(frame, decoded_objects: List, scanned_data: List[str]) -> bool:
    """Process decoded QR codes and update scanned data if new code found."""
    for obj in decoded_objects:
        data = obj.data.decode('utf-8')
        print(f"Data: {data}")
        
        if data in scanned_data:
            print(f'"{data}" already scanned.')
            time.sleep(1)
            return True
        
        scanned_data.append(data)
        print(f"New entry added to database: {data}")
        return True
    return False


def drawQRBoundary(frame, decoded_objects: List) -> None:
    """Draw boundaries around detected QR codes."""
    for obj in decoded_objects:
        points = obj.polygon
        if len(points) > 4:
            hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
            hull = list(map(tuple, np.squeeze(hull)))
        else:
            hull = points
        
        n = len(hull)
        for j in range(n):
            cv2.line(frame, hull[j], hull[(j + 1) % n], (255, 0, 0), 3)


def decodeQRCode() -> None:
    """Main function to decode QR codes from camera feed."""
    print("Press 'q' to quit.")
    
    data_file = os.path.join("saved", "data.json")
    scanned_data = loadData(data_file)

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                continue

            decoded_objects = decode(frame)
            if processDecodedObjects(frame, decoded_objects, scanned_data):
                break

            drawQRBoundary(frame, decoded_objects)
            cv2.imshow("QR Code Scanner", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        cap.release()
        cv2.destroyAllWindows()
        saveData(data_file, scanned_data)
        input("Press Enter to return to main menu...")