import cv2
import numpy as np
from pyzbar.pyzbar import decode
from constants import WINDOW_CLOSE_KEY


def decoder(image):
    gray_img = cv2.cvtColor(image, 0)
    barcode = decode(gray_img)

    for obj in barcode:
        points = obj.polygon
        (x, y, w, h) = obj.rect
        pts = np.array(points, np.int32)
        pts = pts.reshape((-1, 1, 2))
        cv2.polylines(image, [pts], True, (0, 255, 0), 3)

        barcodeData = obj.data.decode("utf-8")
        barcodeType = obj.type
        string = f"Data: {barcodeData} | Type: {barcodeType}"

        cv2.putText(
            frame, string, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2
        )
        string2 = f"Barcode: {barcodeData} | Type: {barcodeType}"
        print(string2)


cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    decoder(frame)
    cv2.imshow("scanner", frame)
    code = cv2.waitKey(10)
    if code == WINDOW_CLOSE_KEY:
        break
