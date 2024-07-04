# Face Recognition Module

This repository contains a Python script for real-time face recognition using OpenCV and DeepFace. The script captures video from the webcam, processes each frame, and checks for a face match against a reference image.

## Features

- Real-time video capture from the webcam.
- Face recognition using DeepFace.
- Multithreading for non-blocking face verification.
- Visual feedback on the video stream indicating whether a face match was found.

## Requirements

- Python 3.6+
- OpenCV
- DeepFace

## Installation

1. Clone the repository:

   `git clone https://github.com/yourusername/face-recognition-module.git
   cd face-recognition-module`

3. Create a virtual environment and activate it:
   
    `python -m venv venv source venv/bin/activate`  
  
   - On Windows, use `venv\Scripts\activate`

3. Install the required packages:

    `pip install -r requirements.txt`

4. Ensure you have a reference image named reference.jpg in the project directory. This image will be used for face matching.'

## Usage

Run the script:
    `python3 main.py`

The script will open a window displaying the video feed from your webcam. The text "MATCH" or "NO MATCH" will be displayed on the video stream to indicate whether a face match was found.

## Code Explanation

### Class: `FaceRecognition`

#### Methods:

- `__init__(self)`: Initializes the video capture, sets frame dimensions, and loads the reference image.
- `check_face(self, frame)`: Verifies if the captured frame matches the reference image using DeepFace.
- `main_job(self)`: Main loop for capturing video frames, running face recognition in a separate thread, and displaying the results.

### Main Execution

The script creates an instance of the `FaceRecognition` class and runs the `main_job` method to start the video capture and face recognition process.

## Example Output

![no_match](https://github.com/EugeneSeverin/face_recognition/assets/106474830/12403e80-58fb-4664-a4fe-6aa45c7b902e)

![image](https://github.com/EugeneSeverin/face_recognition/assets/106474830/e3c55b96-4a68-42c2-b1cb-22c9af361151)


## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.
This markdown includes the explanations and sections you requested. Replace examp


