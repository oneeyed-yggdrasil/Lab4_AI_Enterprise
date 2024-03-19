from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import numpy as np
import joblib

app = Flask(__name__)


model = joblib.load("fish_weight_prediction_model.pkl")

# Define routes
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    # Get input values from the form
    features = [float(x) for x in request.form.values()]
    final_features = [np.array(features)]
    prediction = model.predict(final_features)
    return render_template('index.html', prediction_text = 'Predicted Value: {}'.format(round(prediction[0],3)))

    # length1 = float(request.form['length1'])
    # length2 = float(request.form['length2'])
    # length3 = float(request.form['length3'])
    # height = float(request.form['height'])
    # width = float(request.form['width'])
    
    # # Make prediction
    # prediction = model.predict([[length1, length2, length3, height, width]])
    
    # # Return prediction as JSON
    # return jsonify({'weight': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
