#MathewJV
#Simulación y control de movimiento de robot FANUC

import math
import cv2
import mediapipe as mp
from robodk import robolink

RDK = robolink.Robolink()
robot = RDK.Item('Fanuc M-10iA', robolink.ITEM_TYPE_ROBOT)
if not robot.Valid():
    raise Exception("No se encontró el robot M-10iA en RoboDK")

# Captura de video y Mediapipe
cap = cv2.VideoCapture(1)
hands = mp.solutions.hands.Hands(min_detection_confidence=0.9, min_tracking_confidence=0.8)
mp_drawing = mp.solutions.drawing_utils

# Matriz de control de movimiento
controls = {
    0: {'tip': 4, 'base': 20, 'min_angle': -180, 'max_angle': 180, 'min_dist': 10, 'max_dist': 300},
    1: {'tip': 5, 'base': 8, 'min_angle': -90, 'max_angle': 160, 'min_dist': 15, 'max_dist': 200},
    2: {'tip': 9, 'base': 12, 'min_angle': -95, 'max_angle': 180, 'min_dist': 10, 'max_dist': 250},
    3: {'tip': 13, 'base': 16, 'min_angle': -190, 'max_angle': 190, 'min_dist': 10, 'max_dist': 250},
    4: {'tip': 17, 'base': 20, 'min_angle': -190, 'max_angle': 190, 'min_dist': 10, 'max_dist': 250},
    5: {'tip': 17, 'base': 5, 'min_angle': -360, 'max_angle': 360, 'min_dist': 10, 'max_dist': 250}
}


#Mapeo de distancias
def calculate_angle(tip, base, img_shape, control):
    h, w, _ = img_shape
    x_tip, y_tip = int(tip.x * w), int(tip.y * h)
    x_base, y_base = int(base.x * w), int(base.y * h)

    dist = math.hypot(x_tip - x_base, y_tip - y_base)
    angle = (dist - control['min_dist']) / (control['max_dist'] - control['min_dist']) * (
                control['max_angle'] - control['min_angle']) + control['min_angle']

    return max(min(angle, control['max_angle']), control['min_angle'])


while True:
    success, img = cap.read()
    if not success:
        break

    results = hands.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            joints = robot.Joints().list()

            # Mover ejes
            for axis, control in controls.items():
                tip = hand_landmarks.landmark[control['tip']]
                base = hand_landmarks.landmark[control['base']]
                joints[axis] = calculate_angle(tip, base, img.shape, control)

            robot.MoveJ(joints)
            print("Ángulos de los ejes:", joints)

            mp_drawing.draw_landmarks(img, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)

    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == 27:  # Salir con 'Esc'
        break

cap.release()
cv2.destroyAllWindows()
