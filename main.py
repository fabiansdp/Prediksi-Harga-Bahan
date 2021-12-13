from flask import Flask, render_template, request
import pickle
import locale

app = Flask(__name__)

kategoriDict = {
    "cereals": 0,
    "meat": 1,
    "milk": 2,
    "misc": 3,
    "non-food": 4,
    "oils": 5,
    "veggies": 6
}

komoditasDict = {
    "chili": 0,
    "eggs": 6,
    "kerosene": 8,
    "garlic": 9,
    "beef": 11,
    "chicken": 14,
    "milk": 16,
    "vegetable-oil": 17,
    "shallot": 20,
    "rice": 22,
    "sugar": 26,
    "wheat": 29
}

unitDict = {
    "g": 0,
    "kg": 1,
    "l": 2
}

pricetypeDict = {
    "actual": 0,
    "aggregate": 1
}

def load_model(model_name):
    with open("models/"+model_name+".pkl", 'rb') as file:
        model = pickle.load(file)
    return model

def monthYear(month, year):
    return [int(month), int(year)]

def kategoriArr(kategori):
    retval = [0,0,0,0,0,0,0]
    if (kategori in kategoriDict):
        retval[kategoriDict[kategori]] = 1

    return retval

def komoditasArr(komoditas):
    retval = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if (komoditas in komoditasDict):
        retval[komoditasDict[komoditas]] = 1

    return retval

def unitArr(unit):
    retval = [0,0,0]
    if (unit in unitDict):
        retval[unitDict[unit]] = 1

    return retval

def pricetypeArr(pricetype):
    retval = [0,0]
    if (pricetype in pricetypeDict):
        retval[pricetypeDict[pricetype]] = 1

    return retval

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=["POST"])
def predict():
    if request.method == "POST":
        model_name = request.form['model']
        month = request.form['month']
        year = request.form['year']
        kategori = request.form['kategori']
        komoditas = request.form['komoditas']
        unit = request.form['unit']
        pricetype = request.form['pricetype']
        model = load_model(model_name)

        predictQuery = [monthYear(month, year) + kategoriArr(kategori) + komoditasArr(komoditas) + unitArr(unit) + pricetypeArr(pricetype)]
        
        pricePrediction = model.predict(predictQuery)

        return {    
            "price": "Rp" + str(round(pricePrediction[0], 2))
        }