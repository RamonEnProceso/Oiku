import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL is None:
    raise RuntimeError("Falta la variable de entorno DATABASE_URL")

engine = create_engine(DATABASE_URL)