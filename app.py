from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

app = Flask(__name__)

# Load the dataset
fish_data = pd.read_csv("Fish.csv", sep=",")

# Separate features and target variable
X = fish_data.drop(columns=['Species', 'Weight'])
y = fish_data['Weight']

# Initialize and train the model
model = LinearRegression()
model.fit(X, y)

# Define routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get input values from the form
    length1 = float(request.form['length1'])
    length2 = float(request.form['length2'])
    length3 = float(request.form['length3'])
    height = float(request.form['height'])
    width = float(request.form['width'])
    
    # Make prediction
    prediction = model.predict([[length1, length2, length3, height, width]])
    
    # Return prediction as JSON
    return jsonify({'weight': prediction[0]})

if __name__ == '__main__':
    app.run(debug=True)
