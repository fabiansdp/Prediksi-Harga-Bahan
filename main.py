from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

def load_model(model_name):
    with open("models/"+model_name+".pkl", 'rb') as file:
        model = pickle.load(file)
    return model

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=["POST"])
def predict():
    if request.method == "POST":
        model_name = request.form['model']
        model = load_model(model_name)
        return {
            "test": "Test"
        }