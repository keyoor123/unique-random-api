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

The project follows a clean, modular structure to separate concerns.
```
unique-random-api/
├── app/
│ ├── main.py # API setup and routing
│ ├── generator.py # Random number generation logic
│ └── storage.py # JSON file read/write logic
├── data/
│ └── used_numbers.json # File storing previously returned numbers
├── requirements.txt
└── README.md 
``` 
---

## 4 Tech Stack

-  Python 3.7+
-  FastAPI
-  Uvicorn (ASGI server)
-  JSON file-based persistence

---

## 5 Setup and Installation

### Prerequisites

- Python 3.7 or higher installed
- `pip` package manager

### 1 Clone or Download the Repository

If you're using Git
```
git clone https://github.com/yourusername/unique-random-api.git
cd unique-random-api
```

### 2 Install Dependencies

Install all required Python libraries
```
pip install -r requirements.txt
```

### 3 Run the Server

Start the FastAPI server using Uvicorn

```
uvicorn app.main:app --reload
```

### 4 Access the API

Visit the random number endpoint
```
http://127.0.0.1:8000/random
```

---

## 6 Scalability Ideas

- **Better Storage**: Upgrade from JSON to SQLite or Redis for handling large datasets.
- **Efficient Lookup**: Use sets or hash maps to keep lookup fast even with millions of entries.
- **Sharding**: Split number ranges across services for distributed scalability.
- **Monitoring**: Add `/health` or `/stats` endpoints and integrate logging for observability.
