from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import gunicorn
from pydantic import BaseModel
from model_australian import predict_helper_australian
from model_german import predict_helper_german
import numpy as np

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# pydantic models


class request_body_australian(BaseModel):
    param1: int
    param2: float
    param3: float
    param4: int
    param5: int
    param6: int
    param7: float
    param8: int
    param9: int
    param10: int
    param11: int
    param12: int
    param13: int
    param14: int


class request_body_german(BaseModel):
    employ: str
    age: int
    amount: int
    duration: int
    checkingstatus: str
    history: str
    purpose: str
    savings: str
    status: str


@app.get("/")
def welcome():
    return {"ping": "Hello COBRA. Go to /docs to see the Swagger documentation"}


@app.post("/predict_australian", status_code=200)
def get_prediction_australian(data: request_body_australian):
    '''
    Get prediction for Australian Dataset using COBRA. The accuracy is 85.07%. 
    Sending a JSON query to this end point will give a response of 0 or 1.
    '''
    print(data)

    prediction = predict_helper_australian(
        data.param1,
        data.param2,
        data.param3,
        data.param4,
        data.param5,
        data.param6,
        data.param7,
        data.param8,
        data.param9,
        data.param10,
        data.param11,
        data.param12,
        data.param13,
        data.param14,
    )

    if not prediction:
        raise HTTPException(status_code=400, detail="Model not found.")

    return prediction


@app.post("/predict_german", status_code=200)
def get_prediction_german(data: request_body_german):
    '''
    Get prediction for German Dataset using COBRA. The accuracy is 70.37%. 
    Sending a JSON query to this end point will give a JSON object.
    '''
    print(data)

    prediction_json = predict_helper_german(
        data.employ,
        data.age,
        data.amount,
        data.duration,
        data.checkingstatus,
        data.history,
        data.purpose,
        data.savings,
        data.status,
    )

    if not prediction_json:
        raise HTTPException(status_code=400, detail="Model not found.")

    return prediction_json
