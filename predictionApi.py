from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import Person
import pickle

app = FastAPI()
origins = [
    "https://react-prediction-graphics.herokuapp.com",
    "http://localhost:3000",
    "http://localhost:4200"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

filename = './DTR_Model_test_beck.pkl'
model = pickle.load(open(filename,"rb"))

@app.post("/get-prediction")
def getPrediction(person: Person):
    received = person.dict()
    std_attr = [[
        received["age"],
        received["bmi"],
        received["total_test_beck"],
    ]]
    anxiety_severity = model.predict(std_attr).tolist()[0]
    result = ""
    if anxiety_severity == 0:
        result = "No tiene ansiedad"
    elif anxiety_severity == 1:
        result = "El nivel de Ansiedad detectada es : None-minimal, minima"
    elif anxiety_severity == 2:
        result = "El nivel de Ansiedad detectada es : Mild, Leve"
    elif anxiety_severity == 3:
        result = "El nivel de Ansiedad detectada es : Moderate, Moderada"
    elif anxiety_severity == 4:
        result = "El nivel de Ansiedad detectada es : Severe, severa"
    return result
