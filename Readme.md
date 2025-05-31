## Gesture Volume Control

## Overview

Gesture Volume Control is a Python-based application that allows users to adjust their computer's system volume using hand gestures. By leveraging computer vision, the application detects hand landmarks via a webcam and interprets the distance between the thumb and index finger to control volume levels. This project uses OpenCV for image processing, MediaPipe for hand tracking, and Pycaw for system volume control on Windows.

## Features

* __Real-time Hand Tracking:__ Detects hand gestures using a webcam with MediaPipe's hand tracking solution.


* __Volume Adjustment:__ Adjusts system volume based on the distance between the thumb and index finger.


* __Visual Feedback:__ Displays a volume bar and percentage on the screen for user feedback.


* __Gesture-Based Control:__ Optionally uses specific gestures (e.g., pinky finger down) to set the volume.

## Prerequisites

* Python 3.7 or higher

* A webcam connected to your computer

* Windows operating system (for Pycaw compatibility; alternatives like osascript can be used for macOS)

## Installation

1. __Clone the Repository:__
~~~bash
git clone https://github.com/your-username/Gesture-Volume-Control.git
cd Gesture-Volume-Control
~~~



2. __Install Dependencies:__ Install the required Python libraries using pip:
~~~bash
pip install opencv-python mediapipe pycaw numpy comtypes
~~~

3. __Verify Webcam:__ Ensure your webcam is functional and accessible by Python. You may need to adjust the webcam index in the code if it doesn't work (e.g., change `cv2.VideoCapture(0)` to `cv2.VideoCapture(1)`).

## Usage

1. __Run the Application:__ Navigate to the project directory and execute the main script:

~~~bash
python VolumeHandControl.py
~~~



2. __Gesture Instructions:__

* Hold your hand in front of the webcam.



* Adjust the distance between your thumb and index finger to change the volume:

  * __Pinch closer:__ Decreases volume.

  * __Spread apart:__ Increases volume.



* (Optional) Fold your pinky finger down to set the volume to the current level shown on the volume bar.



* Press q to quit the application.



3. __Visual Feedback:__

      * A bounding box is drawn around the detected hand.

      * A volume bar and percentage are displayed on the screen to reflect the current volume level.

## Project Structure

`VolumeHandControl.py`: Main script for volume control and gesture detection.

`HandTrackingModule.py`: Module containing hand detection and tracking functions.



`requirements.txt`: List of required Python libraries.

## How It Works





1. __Hand Detection:__ MediaPipe's hand tracking model detects 21 3D hand landmarks in each video frame.



2. __Distance Calculation:__ The Euclidean distance between the thumb tip (landmark 4) and index finger tip (landmark 8) is calculated.



3. __Volume Mapping:__ The distance is mapped to a volume range using numpy.interp to scale it between the system's minimum and maximum volume levels.



4. __System Volume Control:__ The pycaw library interfaces with the Windows audio system to set the volume.



5. __Visual Output:__ OpenCV draws a volume bar and percentage on the video feed for real-time feedback.

## Troubleshooting

* __Webcam Issues:__ If the webcam feed doesn't appear, try changing the webcam index in cv2.VideoCapture().
* __Library Errors:__ Ensure all dependencies are installed correctly. Run pip install -r requirements.txt to verify.
* __Performance Lag:__ Reduce the video resolution or frame rate in the script for better performance on low-end systems.

## Contribution
Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-branch).
3. Make your changes and commit (git commit -m "Add feature").
4. Push to the branch (git push origin feature-branch).
5. Open a pull request with a clear description of your changes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
* MediaPipe for hand tracking solutions.
* OpenCV for image processing.
* Pycaw for Windows audio control.