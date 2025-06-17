from fastapi import FastAPI
from app.generator import get_unique_random

app = FastAPI()  # This creates the FastAPI application

@app.get("/random")  # Define a GET HTTP endpoint at /random
def get_random_number():
    return {"number": get_unique_random()}  # Return a unique random number as JSON
