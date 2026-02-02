from fastapi import FastAPI
from pydantic import BaseModel, Field
from house_model import predict_price

app = FastAPI()

class HouseInput(BaseModel):
    size_m2: int = Field(gt=20, lt=500)
    rooms: int = Field(gt=0, lt=10)
    floor: int = Field(ge=0, lt=50)
    distance_to_center_km: float = Field(gt=0, lt=50)
    
@app.post("/predict")
def predict_house_price(data: HouseInput):
    price = predict_price(
        size_m2=data.size_m2,
        rooms=data.rooms,
        floor=data.floor,
        distance=data.distance_to_center_km
    )
    return {
        "estimated_price": price
    }