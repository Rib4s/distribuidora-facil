from fastapi import FastAPI

app = FastAPI(
    title="Distribuidora Fácil API",
    version="0.1.0"
)


@app.get("/")
def home():
    return {
        "message": "Distribuidora Fácil API"
    }