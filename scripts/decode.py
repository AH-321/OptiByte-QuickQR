import cv2
from pyzbar.pyzbar import decode
import json
import numpy as np
import os
import time

if os.name == 'nt':
    python_interpreter = '.venv\\Scripts\\python.exe'
else:
    python_interpreter = '.venv/bin/python'

def decode_qr_code():
    print("Press 'q' to quit.")
    cap = cv2.VideoCapture(0)
    scanned_data = []

    # Load data from JSON file
    try:
        with open("saved/data.json", "r") as file:
            scanned_data = json.load(file)
    except FileNotFoundError:
        print("ERROR: JSON file not found")
        pass

    # Flag to track if data has been added to JSON
    data_added = False

    while True:
        ret, frame = cap.read()
        if not ret:
            continue

        decoded_objs = decode(frame)
        for obj in decoded_objs:
            data = obj.data.decode('utf-8')
            print("Data:", data)
            if data in scanned_data:
                print(f'"{data}" already scanned.')
                time.sleep(3)
                break
            else:
                scanned_data.append(data)
                print("New entry added to JSON database:", data)
                data_added = True
                time.sleep(2)

        # If data added to JSON or already scanned, break the loop
        if data_added or (decoded_objs and data in scanned_data):
            break

        # Draw rectangle
        for obj in decoded_objs:
            points = obj.polygon
            if len(points) > 4:
                hull = cv2.convexHull(np.array([point for point in points], dtype=np.float32))
                hull = list(map(tuple, np.squeeze(hull)))
            else:
                hull = points
            n = len(hull)
            for j in range(0, n):
                cv2.line(frame, hull[j], hull[(j + 1) % n], (255, 0, 0), 3)

        cv2.imshow("QR Code Scanner", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    # Save the updated data to JSON file
    with open("saved/data.json", "w") as file:
        json.dump(scanned_data, file)

    os.system(f'{python_interpreter} main.py')

decode_qr_code()
