from fastapi import FastAPI
from app.routers.bills import router as router_bills
from app.routers.account import router as router_accounts
from app.routers.category import router as router_category
from app.routers.subcategory import router as router_subcategory

app = FastAPI()

@app.get("/")
def read_root():
    return {"status":"online"}

app.include_router(router_bills)
app.include_router(router_accounts)
app.include_router(router_category)
app.include_router(router_subcategory)