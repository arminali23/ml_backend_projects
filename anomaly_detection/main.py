
from fastapi import FastAPI
from pydantic import BaseModel, Field
from anomaly_model import detect

app = FastAPI(title="Anomaly Detection API", version="1.0.0")


class DetectRequest(BaseModel):
    amount: float = Field(gt=0, lt=100000)
    transactions_last_24h: int = Field(ge=0, lt=1000)
    avg_transaction_amount: float = Field(gt=0, lt=100000)
    score_threshold: float = Field(default=0.0)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/detect")
def detect_anomaly(req: DetectRequest):
    result = detect(
        amount=req.amount,
        tx_count=req.transactions_last_24h,
        avg_amount=req.avg_transaction_amount,
        score_threshold=req.score_threshold
    )
    return result