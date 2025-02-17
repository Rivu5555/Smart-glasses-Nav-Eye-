import cv2
from ultralytics import YOLO
from gtts import gTTS
import os

# Load the YOLOv8 model
model = YOLO("yolov8n.pt")  # Use the smallest YOLO model for fast detection

# Open the camera
cap = cv2.VideoCapture(0)  # 0 is the default webcam

while True:
    ret, frame = cap.read()  # Capture frame from camera
    if not ret:
        continue

    # Run YOLOv8 on the captured frame
    results = model(frame)

    # Extract detected objects
    detected_objects = [model.names[int(box.cls)] for box in results[0].boxes]

    if detected_objects:
        detected_text = "I see " + ", ".join(detected_objects)
        print(detected_text)

        # Convert text to speech
        tts = gTTS(text=detected_text, lang='en')
        tts.save("output.mp3")
        os.system("mpg321 output.mp3")  # Play the audio output

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
