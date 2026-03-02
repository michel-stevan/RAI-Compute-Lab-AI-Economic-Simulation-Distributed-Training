from fastapi import FastAPI
from pydantic import BaseModel
import torch
from model import EconomicModel

app = FastAPI()

model = EconomicModel()
model.load_state_dict(torch.load("economic_model.pt"))
model.eval()

class InputData(BaseModel):
    inflation: float
    shock: int

@app.post("/predict")
def predict(data: InputData):
    x = torch.tensor([[data.inflation, data.shock]], dtype=torch.float32)
    prediction = model(x).detach().numpy().tolist()
    return {
        "prediction": prediction
    }
