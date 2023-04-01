import base64

import cv2


def np2bytes(img):
    ret, buffer = cv2.imencode('.jpg', img)
    return buffer.tobytes()


