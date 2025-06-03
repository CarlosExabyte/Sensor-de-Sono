'''
Este script utiliza os classificadores em cascata do OpenCV (haarcascade para faces e olhos)
para detectar rostos e olhos em uma imagem de entrada.
'''

import cv2 as cv
import numpy as np

# Carrega os classificadores pré-treinados para faces e olhos
face_cascade = cv.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
eye_cascade = cv.CascadeClassifier("haarcascades/haarcascade_eye.xml")

# Lê a imagem de entrada e converte para escala de cinza
img = cv.imread('images/test.jpeg')
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

# Detecta faces na imagem usando o classificador em cascata
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# Itera sobre cada face detectada
for (x, y, w, h) in faces:
    # Desenha um retângulo ao redor da face detectada
    cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Define a região de interesse (ROI) para a face atual
    roi_gray = gray[y:y + h, x:x + w]
    roi_color = img[y:y + h, x:x + w]

    # Detecta olhos dentro da região da face
    eyes = eye_cascade.detectMultiScale(roi_gray)

    # Itera sobre cada olho detectado
    for (ex, ey, ew, eh) in eyes:
        # Desenha um retângulo ao redor de cada olho detectado
        cv.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

# Exibe a imagem com as detecções
cv.imshow('Image', img)
cv.waitKey(0)
cv.destroyAllWindows()