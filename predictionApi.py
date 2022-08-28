from fastapi import FastAPI
import pickle
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
origins = [
    "https://react-prediction-graphics.herokuapp.com",
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

filename = './DTR_Model_test_beck.pkl'
model = pickle.load(open(filename,"rb"))

@app.post("/get-prediction")
def getPrediction(age: int, bmi: float, total_test_beck: float):
    anxiety_severity = model.predict([[age, bmi, total_test_beck]])
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
