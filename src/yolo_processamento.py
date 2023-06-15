
from ultralytics import YOLO
import cv2 as cv
import base64
import numpy as np

def Processamento(imagem_base64):
    print("Entrou na função Processamento")
    _, imagem_base64 = imagem_base64.split(',', 1)
    imagem_bytes = base64.b64decode(imagem_base64)
    model = YOLO("best.pt")
    frame = cv.imdecode(np.frombuffer(imagem_bytes, np.uint8), -1)
    result = model.predict(frame, conf=0.5)
    processed_image = result[0].plot()

    # Converta a imagem processada para base64
    _, encoded_image = cv.imencode('.jpg', processed_image)
    imagem_base64 = base64.b64encode(encoded_image).decode('utf-8')
    print("Saiu da função Processamento")
    return imagem_base64