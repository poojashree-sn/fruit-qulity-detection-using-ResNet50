🍎 Fruit Quality Detection Using ResNet50

📌 Project Overview

This project implements a Fruit and Vegetable Quality Detection System using Deep Learning (ResNet50).
The model classifies fruits based on their quality (such as fresh or spoiled) from uploaded images.

A Flask web application is built to provide a simple UI where users can upload an image and receive real-time predictions.

🧠 ResNet50 Explanation

ResNet50 is a 50-layer deep Residual Neural Network that uses skip (residual) connections to overcome vanishing gradient problems.

Why ResNet50?
        
        *Pre-trained on ImageNet
        
        *Excellent for image classification
        
        *Faster convergence using transfer learning
        
        *High accuracy and strong feature extraction

In this project:

        -ResNet50 is used as a base model
        
        -Custom dense layers are added for classification

⚙️ Model & Dataset Note

🚫 The dataset and trained model file are not included in this repository due to GitHub size limitations.

Details:

Model file: fruit_veg_quality_model.h5 ( >100 MB )

Dataset contains categorized fruit & vegetable images

📌 Note:
The dataset and trained model can be shared via Google Drive upon request.

🛠️ Tech Stack

Python

TensorFlow / Keras

ResNet50 (CNN)

Flask

HTML, CSS, JavaScript

OpenCV, NumPy

fruit-qulity-detection-using-ResNet50/
│
├── app.py
├── check.py
├── split_dataset.py
├── static/
│   ├── style.css
│   └── preview.js
├── templates/
│   └── index.html
├── .gitignore
└── README.md
