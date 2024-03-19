from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)

# Load the trained model
model = joblib.load("fish_weight_prediction_model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    features = [float(x) for x in request.form.values()]  # Assuming inputs are provided through a form
    prediction = model.predict([features])[0]
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
