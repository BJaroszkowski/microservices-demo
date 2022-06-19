from api import router
from fastapi import FastAPI

app = FastAPI()

northbound = FastAPI()
northbound.include_router(router)


app.mount("/api", northbound)
