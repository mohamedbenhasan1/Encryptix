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
git clone https://github.com/mohamedbenhasan1/Encryptix/Task_5.git
```
2. Run the script:
```bash
cd Task_5
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
## License

All Rights Reserved. No part of this project may be reproduced, distributed, or modified in any form or by any means without the prior written permission of the project owner.

For inquiries regarding licensing or use permissions, please contact [medbenhasan@gmail.com].
## Author

- **Author Name:** Mohamed Benhasan
- **Email:** medbenhasan@gmail.com
- **LinkedIn:** [Mohamed Benhasan](https://www.linkedin.com/in/mohamed-benhasan-58a78b28a/)
- **GitHub:** [Mohamed Benhasan](https://github.com/mohamedbenhasan1)
