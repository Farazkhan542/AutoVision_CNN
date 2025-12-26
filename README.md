AI Car Classifier – CNN-Based Image Recognition System
📌 Description

This project is an AI-powered web application that classifies car images into different car brands/models using a Convolutional Neural Network (CNN). The system allows users to upload a car image through a web interface and predicts the car model along with a confidence score. The application is built using Flask for the backend and TensorFlow/Keras for deep learning.

⚙️ Technologies Used

Python

Flask

TensorFlow / Keras

NumPy

HTML / CSS

🧠 Model Information

Model Type: Convolutional Neural Network (CNN)

Input Image Size: 128 × 128

Trained Model File: new_car_model.h5

Supported Classes

Audi

Hyundai Creta

Mahindra Scorpio

Rolls Royce

Swift

Tata Safari

Toyota Innova

🚀 Features

Upload car images through a web interface

Automatic image preprocessing and normalization

Real-time prediction using a trained CNN model

Displays predicted car model with confidence percentage

Simple and user-friendly interface

📂 Project Structure
├── app.py
├── new_car_model.h5
├── static/
│   └── uploaded images
├── templates/
│   ├── index.html
│   ├── upload.html
│   └── result.html

▶️ How to Run the Project
Step 1: Install Required Libraries
pip install flask tensorflow numpy

Step 2: Run the Application
python app.py

Step 3: Open in Browser
http://127.0.0.1:5000/

📷 How It Works

User uploads a car image.

The image is resized to 128×128 and normalized.

The CNN model processes the image.

The predicted car model and confidence score are displayed.

🎯 Use Cases

AI and Machine Learning learning project

Demonstration of CNN-based image classification

Portfolio project for AI/ML internships

Web-based deep learning application

🔮 Future Enhancements

Add more car categories

Improve model accuracy with a larger dataset

Deploy the application on cloud platforms

Enhance UI with drag-and-drop upload

👩‍💻 Author

Muhammad Faraz Khan
