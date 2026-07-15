from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__)

model = joblib.load("model.pkl")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/predict")
def predict():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def prediction():

    values = [
        float(request.form["ID"]),
        float(request.form["CODE_GENDER"]),
        float(request.form["FLAG_OWN_CAR"]),
        float(request.form["FLAG_OWN_REALTY"]),
        float(request.form["CNT_CHILDREN"]),
        float(request.form["AMT_INCOME_TOTAL"]),
        float(request.form["NAME_INCOME_TYPE"]),
        float(request.form["NAME_EDUCATION_TYPE"]),
        float(request.form["NAME_FAMILY_STATUS"]),
        float(request.form["NAME_HOUSING_TYPE"]),
        float(request.form["DAYS_BIRTH"]),
        float(request.form["DAYS_EMPLOYED"]),
        float(request.form["FLAG_MOBIL"]),
        float(request.form["FLAG_WORK_PHONE"]),
        float(request.form["FLAG_PHONE"]),
        float(request.form["FLAG_EMAIL"]),
        float(request.form["CNT_FAM_MEMBERS"]),
        float(request.form["CNT_DEPENDENTS"]),
        float(request.form["MONTHS_BALANCE"])
    ]

    prediction = model.predict([values])[0]

    if prediction == 1:
        result = "Credit Card Approved"
    else:
        result = "Credit Card Rejected"

    return render_template("result.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)