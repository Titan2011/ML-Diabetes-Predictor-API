from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from pickle import *
from json import *

a = FastAPI()

o = ["*"]

a.add_middleware(
    CORSMiddleware,
    allow_origins=o,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


class modelInput(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int


diabetesModel = load(open('diabetesModel.sav', 'rb'))


@app.post('/diabetesPrediction')
def diabetesPred(inp: modelInput):
    inputData = inp.json()
    inpDict = loads(inputData)

    p = inpDict['Pregnancies']
    g = inpDict['Glucose']
    bp = inpDict['BloodPressure']
    s = inpDict['SkinThickness']
    ins = inpDict['Insulin']
    bmi = inpDict['BMI']
    dp = inpDict['DiabetesPedigreeFunction']
    age = inpDict['Age']

    inpList = [p, g, bp, s, ins, bmi, dp, age]

    ypred = diabetesModel.predict(inpList)

    if ypred[0] == 0:
        return 'You are not diabetic'

    else:
        return 'You are diabetic'
if __name__ == '__main__':
    uvicorn.run(app, port=8000)
