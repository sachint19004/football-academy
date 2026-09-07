from fastapi import FastAPI

app = FastAPI(title="Football Academy API")


@app.get("/")
def root():
    return {"message": "Football Academy API is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}