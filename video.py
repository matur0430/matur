#https://docs.salad.com/container-engine/guides/yolov8/deployment-tutorial
from ultralytics import YOLO #pip install ultralytics
import cv2 #pip install opencv-python
from cap_from_youtube import cap_from_youtube #pip install ap_from_youtube

# Load the YOLOv8 model
model = YOLO("yolov8n.pt")

# Open youtube video
link = "https://www.youtube.com/watch?v=bMe7f6fxe88"
cap = cap_from_youtube(link, "720p")

# Loop through the video frames
while cap.isOpened():
    # Read a frame from the video
    success, frame = cap.read()
    if success:
        # Run YOLOv8 inference on the frame
        results = model(frame, conf=0.3)
        
        # Visualize the results on the frame
        annotated_frame = results[0].plot()
        
        # Display the annotated frame
        cv2.imshow("YOLOv8 Inference", annotated_frame)
        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        # Break the loop if the end of the video is reached
        break
# Release the video capture object and close the display window
cap.release()
cv2.destroyAllWindows()
print(results[0])