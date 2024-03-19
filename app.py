
from flask import Flask, render_template, request
import your_model  # Import your trained machine learning model
app = Flask(__name__)
@app.route("/")

def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])

def predict():    
    user_input = request.form["user_input"]    
    prediction = your_model.predict(user_input)  # Call model prediction functionreturn render_template("result.html", prediction=prediction)
    
    
if __name__ == "__main__":
    app.run(debug=True)  # Remove debug=True before deployment