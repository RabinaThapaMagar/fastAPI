from fastapi import  FastAPI
from pydantic import BaseModel  ##model lai data pydantic ko through bata dinxan data model lai
import joblib
import numpy as np


app = FastAPI() 

#loading the model
model = joblib.load('saved/DecisionTreePrediction.pkl')

#datako type milauna parxa using pydantic

#Glucose
#BloodPressure
#DFP
#AGE

#datako lagi class create garne
class Patient(BaseModel) :
    Glucose: float
    BloodPressure: int
    DiabetesPedigreeFunction : float
    Age : int


@app.get('/')## route banako mathiko app object use garera
def show(): ## show vaney function
    return{'message': 'Hello Guys'}



@app.get('/about')
def about():
    return{'Display':'Broad AI is a education Sector'}

@app.post('/predict')
async def predict(data:Patient): #async asynchronouse banako function ko name ko agadi
    input_data = np.array([[
        data.Glucose, data.BloodPressure, data.DiabetesPedigreeFunction, data.Age

   ]]) 
    prediction = await model.predict(input_data)[0] #await ie free time payo bhaney arko lai ready banaune for prediction
    return {"prediction": int(prediction)}



