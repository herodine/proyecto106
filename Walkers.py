import cv2
import numpy as np

# Crear nuestro clasificador de cuerpos
body_classifier = cv2.CascadeClassifier('haarcascade_fullbody.xml')

# Inicializar la captura de video para nuestro archivo de video
cap = cv2.VideoCapture('walking.avi')

# Comenzar el bucle una vez que el video esté cargado exitosamente
while True:
    
    # Leer el primer cuadro
    ret, frame = cap.read()
    #frame = cv2.resize(frame, None,fx=0.5, fy=0.5, interpolation = cv2.INTER_LINEAR)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Pasar el cuadro a nuestro clasificador de cuerpos
    bodies = body_classifier.detectMultiScale(gray, 1.2, 3)
    
    # Extraer las cajas envolventes para cualquier cuerpo identificado
    for (x,y,w,h) in bodies:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
        cv2.imshow('Peatones', frame)

    if cv2.waitKey(1) == 32: #32 es la barra espaciadora
        break

cap.release()
cv2.destroyAllWindows()
