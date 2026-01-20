from flask import Flask, render_template, request
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

app = Flask(__name__)

# Load trained model
model = load_model("fruit_veg_quality_model.h5")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    file = request.files.get("file")

    if not file or file.filename == "":
        return render_template("index.html", result="No file selected")

    img_path = "temp.jpg"
    file.save(img_path)

    # Load and preprocess image
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    # Prediction
    pred = model.predict(img_array)[0][0]

    # Correct class mapping:
    # fresh = 0, rotten = 1
    if pred >= 0.3:
        label = "🍎 Rotten"
        confidence = pred
    elif 0.9<pred<=1:
        label="not fruit please upload fruit image"
        confidence=pred
    
    else:
        label = "🍏 Fresh"
        confidence = 1 - pred
    return render_template(
        "index.html",
        result=label,
        confidence=f"{confidence:.2f}"
    
    )


if __name__ == "__main__":
    app.run(debug=True)
