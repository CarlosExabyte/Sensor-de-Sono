'''
Este script utiliza os classificadores em cascata do OpenCV (haarcascade para faces e olhos)
para detectar rostos e olhos em um feed de vídeo capturado pela webcam.
'''

# Importa as bibliotecas necessárias
import cv2 as cv
import numpy as np

# Carrega os classificadores pré-treinados para faces e olhos
face_cascade = cv.CascadeClassifier("haarcascades/haarcascade_frontalface_default.xml")
eye_cascade = cv.CascadeClassifier("haarcascades/haarcascade_eye.xml")

# Inicia a captura de vídeo da webcam
video_capture = cv.VideoCapture(0)

# Processa cada frame do vídeo em tempo real
while True:
    ret, frame = video_capture.read()
    frame = cv.flip(frame, 1)  # Espelha o frame para parecer um espelho
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    # Detecta faces no frame atual
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # Processa cada face detectada
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # Detecta olhos dentro da região da face
        eyes = eye_cascade.detectMultiScale(roi_gray)

        # Desenha retângulos ao redor dos olhos detectados
        for (ex, ey, ew, eh) in eyes:
            cv.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)

    # Exibe o frame com as detecções
    cv.imshow('Video', frame)

    # Encerra o loop se a tecla 'q' for pressionada
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Libera os recursos da câmera e fecha todas as janelas
video_capture.release()
cv.destroyAllWindows()