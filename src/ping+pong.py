import cv2
import mediapipe as mp

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands
import matplotlib.pyplot as plt
import random

x_circle = 600
y_circle = 450

count = 0

# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
model_complexity=0,
min_detection_confidence=0.5,
min_tracking_confidence=0.5) as hands:
while cap.isOpened():
success, image = cap.read()
if not success:
print("Ignoring empty camera frame.")
# If loading a video, use 'break' instead of 'continue'.
continue

# To improve performance, optionally mark the image as not writeable to
# pass by reference.
image.flags.writeable = False
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
results = hands.process(image)

# Draw the hand annotations on the image.
image.flags.writeable = True
image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
if results.multi_hand_landmarks:
for hand_landmarks in results.multi_hand_landmarks:

height = image.shape[0]
width = image.shape[1]

x = round(hand_landmarks.landmark[8].x * width)
y = round(hand_landmarks.landmark[8].y * height)

print(x, y)

# if left print left

if x > 350:

cv2.line(image, (625, y - 50), (625, y + 50), (0, 255, 0), thickness=5)
plt.imshow(image)
else:
cv2.line(image, (20, y - 50), (20, y + 50), (0, 255, 0), thickness=5)
plt.imshow(image)

# bouncing ball

cv2.circle(img=image, center=(x_circle, y_circle), radius=15, color=(255, 0, 0), thickness=10)

if x_circle >= 40 and count != 57:
x_circle -= 10
print("pppp", y_circle)
count += 1


y_circle -= 10
if y_circle < 30:
y_circle *= -1
if x_circle <= 600 and count == 57:
x_circle += 10

y_circle += 10
if y_circle > 450:
y_circle *= -1

if x_circle == 600:
count *= 0

mp_drawing.draw_landmarks(
image,
hand_landmarks,
mp_hands.HAND_CONNECTIONS,
mp_drawing_styles.get_default_hand_landmarks_style(),
mp_drawing_styles.get_default_hand_connections_style())

# Flip the image horizontally for a selfie-view display.
cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
if cv2.waitKey(5) & 0xFF == 27:
break
cap.release()
