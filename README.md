# Real-time-face-detection-using-OpenCV-and-Haar-Cascades
Its a face recognition application which can detect two or more faces which might be present in the camera lens view.
Overview
This Python code demonstrates real-time face detection using the OpenCV library. It captures video from your computer's default webcam and applies the Haar Cascade classifier for detecting faces in each frame. Detected faces are highlighted with blue rectangles, providing a simple but effective face recognition mechanism.

Prerequisites
Before using this code, make sure you have the following prerequisites:

Python: Ensure that Python is installed on your system. You can download Python from the official website.

OpenCV: Install OpenCV, a popular computer vision library, using pip with the following command:

shell
Copy code
pip install opencv-python
Usage
Clone or download this repository to your local machine.

Open a terminal or command prompt and navigate to the directory containing the code.

Run the script by executing the following command:

shell
Copy code
python your_script_name.py
The code will open your computer's default webcam and display the video feed in a window. Detected faces will be outlined with blue rectangles.

To exit the program, press the 'q' key in the video window.

Description
Video Capture
The code starts by capturing video from the default webcam using OpenCV's VideoCapture object. If the capture device cannot be opened, an error message is displayed.

Face Detection
The Haar Cascade classifier for face detection is loaded using cv2.CascadeClassifier. This classifier is pre-trained and provided by OpenCV.

Inside the main loop, each frame from the video feed is converted to grayscale to simplify face detection. The detectMultiScale method is then applied to identify faces in the frame. Detected faces are represented as a set of coordinates (x, y, width, height), and blue rectangles are drawn around them using OpenCV's rectangle function.

Real-Time Display
The processed frame with detected faces is displayed in a window labeled "Face recognition" using cv2.imshow. The program continues to run until you press the 'q' key, at which point the loop breaks.

Cleanup
After exiting the loop, the video capture is released using cap.release(), and the OpenCV windows are destroyed with cv2.destroyAllWindows().
