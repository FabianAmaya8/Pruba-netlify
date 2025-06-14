from dotenv import load_dotenv
import os

# Carga variables del archivo .env
load_dotenv()

class Config:
    SECRET_KEY = 'CLAVE'
    PG_HOST = os.getenv("PG_HOST")
    PG_USER = os.getenv("PG_USER")
    PG_PASSWORD = os.getenv("PG_PASSWORD")
    PG_DB = os.getenv("PG_DB")
    PG_PORT = int(os.getenv("PG_PORT", 5432))
    SESSION_COOKIE_SECURE = False
