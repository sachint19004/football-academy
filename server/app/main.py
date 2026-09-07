from fastapi import FastAPI

app = FastAPI(title="Football Academy API")


@app.get("/health")
def health_check():
    return {"status": "ok"}