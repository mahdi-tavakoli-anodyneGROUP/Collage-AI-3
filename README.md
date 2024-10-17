# OPG Dental Image Labeling Project Using Roboflow and YOLOv8

A model trained by YOLO v8 using Roboflow.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

This project is designed for labeling OPG dental images. It utilizes Roboflow for labeling and YOLOv8 for training the model.

## Prerequisites
To run this project, you need the following software and libraries:
- Python 3.x
- Roboflow and YOLOv8 libraries
- Other necessary libraries (like NumPy, OpenCV, etc.)

## Installation

You can install the required libraries using pip:

   ```bash
   pip install roboflow
   pip install ultralytics
   ```

## Usage
1 - Labeling Images:
 - First, upload the OPG images to Roboflow.
 - Use the available tools to label the images.
2 - Training the Model:
 - Use the YOLOv8 model to train on the labeled data.
 - Run the following code for training:
```python
   from ultralytics import YOLO

   model = YOLO('yolov8n.pt')  # Base YOLOv8 model
   model.train(data='data.yaml', epochs=50)  # Set the number of training epochs

   ```
## Results

After training, you can use the model to detect and label new images.
## Contributing

If you wish to contribute to this project, please submit your request through Issues on GitHub.
## License

This project is licensed under the [Anodyne License](https://github.com/mahdi-tavakoli-anodyneGROUP/Collage-AI-3.git). 

## Contact

For any inquiries, feel free to reach out:

- **Faraz Tajdar**: [faraz.tajdar2@gmail.com](mailto:faraz.tajdar2@gmail.com)
- **Aryan Oliaee**: [a123.oliaee@gmail.com](mailto:a123.oliaee@gmail.com)
- **GitHub**: [Aryandecoder](https://github.com/Aryandecoder), [farazfx](https://github.com/farazx)

---

Feel free to customize the content to fit your specific project details and requirements!
