from flask import Flask, render_template, request
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os

app = Flask(__name__)

# Load model
model = load_model("new_car_model.h5")

# Class Names (change for your dataset)
class_names = ['Audi','Hyundai Creta','Mahindra Scorpio','Rolls Royes','Swift','Tata Safari', 'Toyota Innova']

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/upload')
def upload_page():
    return render_template('upload.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return "No file uploaded!"

    file = request.files['file']
    filepath = "static/" + file.filename
    file.save(filepath)

    # ---------------------------
    # Preprocess with 128x128 size
    # ---------------------------
    img = image.load_img(filepath, target_size=(128, 128))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # ---------------------------
    # Predict
    # ---------------------------
    prediction = model.predict(img_array)
    index = np.argmax(prediction)
    predicted_class = class_names[index]
    confidence = round(np.max(prediction) * 100, 2)

    return render_template(
        'result.html',
        image_path=filepath,
        predicted=predicted_class,
        confidence=confidence
    )

if __name__ == '__main__':
    app.run(debug=True)
