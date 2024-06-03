# Image Captioning using Deep Learning
This project aims to generate captions for images using deep learning techniques. It utilizes the InceptionV3 model for feature extraction and a combination of LSTM and dense layers for caption generation.

## Setup
1. Clone the repository:
```bash
git clone https://github.com/your-username/Encryptix/Task_2.git
cd Task_2
```
2. Install the required packages:
```bash
pip install -r requirements.txt
```
3. Download the dataset:
- Download the Flickr8k dataset from here.
- Extract the dataset and place it in the project directory.
## Usage
1. Preprocess the dataset:
- Run `preprocess.py` to preprocess the images and captions.
2. Train the model:
- Run `train.py` to train the captioning model.
3. Generate captions:
- Use `generate_caption.py` to generate captions for new images.
## Example
### Generate caption for a new image
```bash
from image_captioning import generate_caption

img_path = 'path/to/your/image.jpg'
caption = generate_caption(img_path)
print("Caption:", caption)
```
## Author
Mohamed Benhasan
