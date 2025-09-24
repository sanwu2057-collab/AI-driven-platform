from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AI-Driven Urban Heat Island Impact Platform API is running."}
