# import the necessary packages
import pytesseract
import argparse
import cv2
import base64
import numpy as np

def ocrImage(image_b64):
    decoded_data = base64.b64decode(image_b64)
    np_data = np.frombuffer(decoded_data,np.uint8)
    img = cv2.imdecode(np_data,cv2.IMREAD_UNCHANGED)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    text = pytesseract.image_to_string(img)
    return text

