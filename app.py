from flask import Flask, render_template, request, jsonify
import joblib

app = Flask(__name__)
model = joblib.load('fish_weight_prediction_model.pkl')

@app.route('/')
def index():
    return render_template('input.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    species = request.json['species']
    length1 = float(request.json['length1'])
    length2 = float(request.json['length2'])
    length3 = float(request.json['length3'])
    height = float(request.json['height'])

    # Make prediction using the model
    prediction = model.predict([[length1, length2, length3, height]])[0]

    # Return prediction as JSON
    return jsonify({'prediction': prediction})

if __name__ == '__main__':
    app.run(debug=True)
