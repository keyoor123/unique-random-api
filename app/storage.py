import json
import os
from typing import Set

DATA_PATH = "data/used_numbers.json"

def load_numbers() -> Set[float]:
    if not os.path.exists(DATA_PATH):
        return set()  # If file doesn't exist, return empty set
    with open(DATA_PATH, "r") as f:
        return set(json.load(f))  # Load and convert list to set

def save_number(num: float):
    numbers = load_numbers()  # Load current numbers
    numbers.add(num)  # Add the new one
    with open(DATA_PATH, "w") as f:
        json.dump(list(numbers), f)  # Save back to file as a list
