from flask import Flask, jsonify, render_template, request
import joblib
import numpy as np


app = Flask(__name__)
MODEL = joblib.load("iris_model.joblib")
CLASS_NAMES = ["setosa", "versicolor", "virginica"]


@app.get("/")
def home():
    return render_template("index.html")


@app.get("/health")
def health():
    return jsonify(status="healthy", model="iris-logistic-regression"), 200


@app.post("/predict")
def predict():
    data = request.get_json(silent=True) or {}
    required = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
    missing = [name for name in required if name not in data]
    if missing:
        return jsonify(error="Missing required fields", missing=missing), 400
    try:
        features = np.array([[float(data[name]) for name in required]])
    except (TypeError, ValueError):
        return jsonify(error="All feature values must be numeric"), 400

    prediction = int(MODEL.predict(features)[0])
    confidence = float(MODEL.predict_proba(features)[0].max())
    return jsonify(
        prediction=prediction,
        class_name=CLASS_NAMES[prediction],
        confidence=round(confidence, 4),
        model_version="1.1.0",
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
