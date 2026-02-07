import numpy as np
from sklearn.ensemble import IsolationForest

X_train = np.array([
    [50, 3, 40],
    [60, 4, 45],
    [55, 2, 38],
    [70, 5, 50],
    [65, 4, 48],
    [80, 6, 55],
])

model = IsolationForest(
    n_estimators=100,
    contamination=0.1,
    random_state=42
)

model.fit(X_train)

def detect(amount, tx_count, avg_amount, score_threshold=0.0):
    X = np.array([[amount, tx_count, avg_amount]])
    score = model.decision_function(X)[0]
    model_flag = model.predict(X)[0] == -1

    custom_flag = score < score_threshold

    return {
        "anomaly_model": model_flag,
        "anomaly_custom": custom_flag,
        "score": float(score),
        "threshold": float(score_threshold),
    }