from fastapi import FastAPI
from app.routers.gastos import router as router_gastos

app = FastAPI()

@app.get("/")
def read_root():
    return {"status":"online"}

app.include_router(router_gastos)
