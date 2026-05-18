from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def display():
    return {"Hello": "World"}


"""
uvicorn main:app --reload
INFO: Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO: Started reloader process [28720]
INFO: Started server process [28722]
INFO: Waiting for application startup.
INFO: Application startup complete.

http://localhost:/8000

"""