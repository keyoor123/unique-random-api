import random
from app.storage import load_numbers, save_number

def get_unique_random() -> float:
    used_numbers = load_numbers()  # Load previously used numbers from file

    while True:
        num = round(random.uniform(0, 1e6), 6)  # Create a float random number
        if num not in used_numbers:
            save_number(num)  # Save it to persistent storage
            return num  # Return only if it's never been used
