from fastapi import FastAPI

from app.routes.users import router as users_router

app = FastAPI(title="Football Academy API")

app.include_router(users_router)


@app.get("/")
def root():
    return {"message": "Football Academy API is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}