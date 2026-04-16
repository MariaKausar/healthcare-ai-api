from fastapi import FastAPI
from pydantic import BaseModel
from model import predict_risk

app = FastAPI()

class PatientData(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Healthcare AI API is running"}

@app.post("/predict")
def predict(data: PatientData):
    result = predict_risk(data.text)
    return {"risk_level": result}