from fastapi import FastAPI
from api import router

app = FastAPI()

northbound = FastAPI()
northbound.include_router(router)


app.mount("/api", northbound)
