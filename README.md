# Unique Random Number API

An HTTP server with one goal: **return a random number that is globally unique** — even across server restarts.

Built with **FastAPI** and local JSON storage (no external database or API).

---

##  1 Objective

Create a `/random` endpoint that:
- Returns a **random number** (int or float)
- Ensures the number is **never repeated**
- Persists data across restarts

---

## 2 Features

-  **Unique Random Numbers**: Every call to `/random` returns a new, never-before-seen number.
-  **No Repeats**: Guaranteed uniqueness even after server restarts — all used numbers are stored.
-  **Persistent Storage**: Uses a local JSON file to store numbers for durability across sessions.
-  **FastAPI Integration**: Lightweight and high-performance Python web framework.
-  **Modular Codebase**: Separated logic for number generation, storage, and API endpoints.
- **Clean and Readable Code**: Follows Python best practices and clean architecture principles.

---

## 3 Project Structure

```text unique-random-api/ ├── app/ │ ├── main.py # API setup and routing │ ├── generator.py # Random number generation logic │ └── storage.py # JSON file read/write logic ├── data/ │ └── used_numbers.json # File storing previously returned numbers ├── requirements.txt ├── .gitignore └── README.md ``` 

---

## 4 Tech Stack

-  Python 3.7+
-  FastAPI
-  Uvicorn (ASGI server)
-  JSON file-based persistence
