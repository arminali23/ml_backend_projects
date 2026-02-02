import numpy as np
import joblib
from sklearn.linear_model import LinearRegression

X = np.array([
    [50, 1, 1, 10],
    [70, 2, 2, 8],
    [90, 3, 2, 6],
    [120, 3, 3, 4],
    [150, 4, 4, 3],
    [200, 5, 5, 1],
])

y = np.array([150, 200, 260, 350, 450, 650])

model = LinearRegression()
model.fit(X,y)

joblib.dump(model, "house_price_model.joblib")
print("model saved")