import pandas as pd
import joblib 

def test_model_loads():
    model = joblib.load("carmodel.pkl")
    assert model is not None

def test_prediction_runs():
    model = joblib.load("carmodel.pkl")
    sample = pd.DataFrame([{
        "model": "3 Series",
        "year": 2018,
        "mileage": 20000,
        "transmission": "Automatic",
        "fuelType": "Petrol",
        "tax": 150,
        "mpg": 45,
        "engineSize": 2.0
    }])

    sample.columns = sample.columns.str.lower()
    pred = model.predict(sample)
    assert pred[0] > 0