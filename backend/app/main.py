from fastapi import FastAPI

from app.api.v1 import api_router
from app.core.config import settings

app = FastAPI()
app.include_router(api_router, prefix=settings.API_V1_STR)


@app.get("/")
def index():
    return {"Hello": "yyds"}
