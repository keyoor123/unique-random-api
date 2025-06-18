# Unique Random Number API

An HTTP server with one goal: **return a random number that is globally unique** — even across server restarts.

Built with **FastAPI** and local JSON storage (no external database or API).

---

##  Objective

Create a `/random` endpoint that:
- Returns a **random number** (int or float)
- Ensures the number is **never repeated**
- Persists data across restarts

---

##  Tech Stack

-  Python 3.7+
-  FastAPI
-  Uvicorn (ASGI server)
-  JSON file-based persistence
