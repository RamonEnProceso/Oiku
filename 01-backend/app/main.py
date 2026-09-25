from fastapi import FastAPI
from app.routers.bills import router as router_bills

app = FastAPI()

@app.get("/")
def read_root():
    return {"status":"online"}

app.include_router(router_bills)
