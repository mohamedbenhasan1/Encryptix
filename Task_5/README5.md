# Face Detection Application

This application detects faces in images, videos from the webcam, and uploaded video files using OpenCV and pre-trained Haar cascades.

## Features

- **Image Face Detection**: Detects faces in a given image file.
- **Webcam Video Face Detection**: Detects faces in real-time using the webcam.
- **Uploaded Video File Face Detection**: Detects faces in a provided video file.

## Requirements

- Python 3.x
- OpenCV library

## Installation

1. Install Python from the [official website](https://www.python.org/).
2. Install the required OpenCV library using pip:

```bash
pip install opencv-python
```
## Usage
1. Clone the repository or download the script:
```bash
git clone https://github.com/yourusername/face-detection-app.git
cd face-detection-app
```
2. Run the script:
```bash
python facedetect.py
```
3. Choose the input type:
- For images: Enter image and provide the full path to the image file (e.g., C:\Users\Mohamed Benhasan\Pictures\image1.jpg).
- For webcam video: Enter video. The script will access your webcam.
- For uploaded video files: Enter upload and provide the full path to the video file (e.g., C:\Users\Mohamed Benhasan\Videos\video1.mp4).
## Examples
Image Face Detection
```bash
Enter 'video' to use webcam, 'upload' to upload a video file, or 'image' to provide an image path: image
Enter the path to the image (e.g., C:\Users\Mohamed Benhasan\Pictures\image1.jpg): C:\Users\Mohamed Benhasan\Pictures\image1.jpg
```
Webcam Video Face Detection
```bash
Enter 'video' to use webcam, 'upload' to upload a video file, or 'image' to provide an image path: video
```
Uploaded Video File Face Detection
```bash
Enter 'video' to use webcam, 'upload' to upload a video file, or 'image' to provide an image path: upload
Enter the path to the video file (e.g., C:\Users\Mohamed Benhasan\Videos\video1.mp4): C:\Users\Mohamed Benhasan\Videos\video1.mp4
```
- Ensure the provided paths are correct and the files exist.
- The program will display detected faces in real-time for videos and show the image with detected faces for images.
- Press 'q' to quit the video window when using the webcam or video file.
