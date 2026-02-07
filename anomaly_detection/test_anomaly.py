from anomaly_model import detect

tests = [
    ("normal-1", 60, 4, 45),
    ("normal-2", 70, 5, 50),
    ("suspicious-1", 500, 20, 30),   
    ("suspicious-2", 20, 1, 5), 
    ("suspicious-3", 1000, 2, 500),
]

for name, amount, tx, avg in tests :
    res = detect(amount, tx, avg, score_threshold=0.0)
    print(f"{name:12}  model={res['anomaly_model']}  custom={res['anomaly_custom']}  score={res['score']:.4f}")