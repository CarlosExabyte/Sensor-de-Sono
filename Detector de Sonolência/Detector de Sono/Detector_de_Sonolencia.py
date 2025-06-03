from scipy.spatial import distance
from imutils import face_utils
import numpy as np
import pygame
import time
import dlib
import cv2
from datetime import datetime  # Adicionado para manipulação de horários

# Configurações do Pygame para o alarme
pygame.mixer.init()
pygame.mixer.music.load('audio/alert.wav')

# Constantes para detecção de sono
EYE_ASPECT_RATIO_THRESHOLD = 0.3
EYE_ASPECT_RATIO_CONSEC_FRAMES = 50
COUNTER = 0

# Perfis de Alarme (Horários definidos)
PERFIS_ALARME = {
    "manha": {"hora": 9, "minuto": 0},    # 09:00
    "tarde": {"hora": 15, "minuto": 42},   # 15:00
    "noite": {"hora": 23, "minuto": 0}    # 23:00
}

# Função para verificar se é hora do alarme
def verificar_alarme(perfil):
    agora = datetime.now()
    perfil_hora = PERFIS_ALARME[perfil]["hora"]
    perfil_minuto = PERFIS_ALARME[perfil]["minuto"]
    
    if agora.hour == perfil_hora and agora.minute == perfil_minuto:
        return True
    return False

# Função para calcular o Eye Aspect Ratio (EAR)
def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    return (A + B) / (2 * C)

# Inicializa o detector de faces do dlib
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

# Índices para os olhos
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS['left_eye']
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS['right_eye']

# Inicia a webcam
video_capture = cv2.VideoCapture(0)
time.sleep(2)  # Tempo para a câmera inicializar

# Seleção do perfil (pode ser automatizado ou via input)
perfil_ativo = "tarde"  # Altere para "manha", "tarde" ou "noite"

while True:
    ret, frame = video_capture.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Verifica se é hora do alarme do perfil selecionado
    if verificar_alarme(perfil_ativo):
        pygame.mixer.music.play(-1)  # Toca o alarme em loop
        cv2.putText(frame, f"ALARME {perfil_ativo.upper()}!", (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Detecção de sono (código original)
    faces = detector(gray, 0)
    for face in faces:
        shape = predictor(gray, face)
        shape = face_utils.shape_to_np(shape)
        
        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]
        
        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)
        ear = (leftEAR + rightEAR) / 2

        # Desenha contornos dos olhos
        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)
        cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

        # Detecta sono
        if ear < EYE_ASPECT_RATIO_THRESHOLD:
            COUNTER += 1
            if COUNTER >= EYE_ASPECT_RATIO_CONSEC_FRAMES:
                pygame.mixer.music.play(-1)  # Alarme de sono
                cv2.putText(frame, "SONO DETECTADO!", (150, 200),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 2)
        else:
            if not verificar_alarme(perfil_ativo):  # Para o alarme apenas se não for horário programado
                pygame.mixer.music.stop()
            COUNTER = 0

    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()