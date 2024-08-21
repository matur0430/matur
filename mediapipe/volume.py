import cv2
import mediapipe as mp
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import numpy as np

# Initialize MediaPipe Hands
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Initialize VideoCapture
cap = cv2.VideoCapture(0)

# Function to set the system volume
def set_volume(volume_level):
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(
        IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    volume.SetMasterVolumeLevelScalar(volume_level, None)

# Initialize variables for volume control
prev_volume_level = None
min_dist = 10   # Minimum distance for volume control
max_dist = 30   # Maximum distance for volume control

# Define the button area
button_x1, button_y1 = 50, 50
button_x2, button_y2 = 600, 400


box1_x1,box1_y1 = 10,10
box1_x2,box1_y2 = 20,20

with mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
    
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            continue

        # Convert the BGR image to RGB and flip it
        image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
        
        # Process the image and find hand landmarks
        results = hands.process(image)
        
        # Convert the image back to BGR for rendering
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Draw the button on the image
        cv2.rectangle(image, (button_x1, button_y1), (button_x2, button_y2), (0, 255, 0), -1)
        cv2.rectangle(image, (box1_x1, box1_y1), (box1_x2, box1_y2), (0, 0, 0), -1)
        cv2.putText(image, "Adjust Volume Range ", (button_x1 + 20, button_y1 + 50), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                finger1_x = hand_landmarks.landmark[4].x
                finger1_y = hand_landmarks.landmark[4].y
                finger2_x = hand_landmarks.landmark[8].x
                finger2_y = hand_landmarks.landmark[8].y

                # Convert normalized coordinates to pixel coordinates
                h, w, _ = image.shape
                finger1_x_pixel = int(finger1_x * w)
                finger1_y_pixel = int(finger1_y * h)
                finger2_x_pixel = int(finger2_x * w)
                finger2_y_pixel = int(finger2_y * h)
                
                # Check if the finger is within the button area
                if (button_x1 < finger1_x_pixel < button_x2 and button_y1 < finger1_y_pixel < button_y2) or \
                   (button_x1 < finger2_x_pixel < button_x2 and button_y1 < finger2_y_pixel < button_y2):
                    # Calculate the Euclidean distance between the two fingers
                    dist = np.linalg.norm(
                        np.array([finger1_x, finger1_y]) - np.array([finger2_x, finger2_y])
                    )
                    
                    # Map the distance to the volume range (0.0 to 1.0)
                    volume_level = np.interp(dist, [min_dist / 100, max_dist / 100], [0.0, 1.0])
                    
                    # Set the system volume if the volume level has changed significantly
                    if prev_volume_level is None or abs(volume_level - prev_volume_level) > 0.01:
                        set_volume(volume_level)
                        prev_volume_level = volume_level

                    # Display the distance and volume level on the image
                    cv2.putText(
                        image, text=f'Dist={int(dist*100)} Volume={int(volume_level*100)}%', 
                        org=(10, 30),
                        fontFace=cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(255, 0, 0), thickness=3
                    )
                    
                # Draw hand landmarks on the image
                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS
                )
        else:
            # If no hands are detected, keep the previous volume
            if prev_volume_level is not None:
                set_volume(prev_volume_level)

        # Display the image
        cv2.imshow('Volume Control', image)
        
        if cv2.waitKey(1) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
