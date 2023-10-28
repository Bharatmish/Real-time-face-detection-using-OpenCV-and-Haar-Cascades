import cv2

# Capture video from the camera
#cap = cv2.VideoCapture(0)
# Initialize the video capture object using the default webcam
cap = cv2.VideoCapture(0)

# Check if the video capture device was successfully opened
if not cap.isOpened():
    print('Error: Could not open video capture device.')


# Load the Haar cascade file for face detection
face_cascade = cv2.CascadeClassifier('C:\\Users\\Bharat Kumar Mishra\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')

while True:
    # Read each frame from the video capture
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Use the Haar cascade file to detect faces in the frame
    faces = face_cascade.detectMultiScale(gray)

    # Iterate over the detected faces
    for (x, y, w, h) in faces:
        # Draw a rectangle around the face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Show the frame
    cv2.imshow('Face recognition', frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and destroy the windows
cap.release()
cv2.destroyAllWindows()
