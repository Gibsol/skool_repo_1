import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

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
    left_hand_x = 1
    left_hand_y = 1
    right_hand_x = 1
    right_hand_y = 1 
    if results.multi_hand_landmarks:
      for hand_landmarks in results.multi_hand_landmarks:
        x = int(hand_landmarks.landmark[8].x * 640)
        y = int(hand_landmarks.landmark[8].y * 480)
        if x < 480 / 2:
            left_hand_y = y 
            left_hand_x = x 
        else:
            right_hand_y = y 
            right_hand_x = x        

    color = (255, 0, 0)

    cv2.circle(image, (left_hand_x, left_hand_y), 10, color, 2)
    cv2.rectangle(image,(20,left_hand_y),(20,left_hand_y+50),(0,255,0),3)

    cv2.circle(image, (right_hand_x, right_hand_y), 10, color, 2)
    cv2.rectangle(image,(460,right_hand_y),(460,right_hand_y+50),(0,255,0),3)

    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()
