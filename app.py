from fastapi import FastAPI
from typing import Literal
from preprocessing.perprocess import preprocess
import random

app = FastAPI()

@app.get("/")
async def root():
    """Welcoming route!"""
    return "Alive!"

@app.post("/predict")
def predict(
    is_house: bool,
    surface_area: int,
    city: Literal["bruxelles", "charleroi", "ixelles"]
):
    print("Start predicting new price...")
    data = {
        "is_house": is_house,
        "surface_area": surface_area,
        "city": city
    }
    preprocessed_data = preprocess(data)
    print("data preprocessed: ", preprocessed_data)
    price = random.randint(100_000, 1_000_000)
    result = {"prediction": price}
    return result
