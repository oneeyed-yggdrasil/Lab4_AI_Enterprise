from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)

# Load the trained model
model = joblib.load("backend/fish_weight_prediction_model.pkl")

@app.route("/predict", methods=["POST"])
def predict():
    if request.method == "POST":
        # Get data from the request
        data = request.json

        # Extract features
        length1 = data["length1"]
        length2 = data["length2"]
        length3 = data["length3"]
        height = data["height"]
        width = data["width"]

        # Make prediction
        features = np.array([[length1, length2, length3, height, width]])
        prediction = model.predict(features)

        # Prepare response
        response = {"weight": float(prediction)}

        return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)
