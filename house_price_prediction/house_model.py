import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

model = joblib.load("house_price_model.joblib")

def predict_price(size_m2, rooms, floor, distance):
    features = np.array([[size_m2, rooms, floor, distance]])
    price = model.predict(features)[0]
    return round(price * 1000)

def explain_model():
    feature_names = [
        "size_m2",
        "rooms",
        "floor",
        "distance_to_center_km"
    ]
    
    for name, coef in zip(feature_names, model.coef_):
        print(f"{name}: {round(coef * 1000)} TL")