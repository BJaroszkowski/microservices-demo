from pydantic import BaseModel


class Result(BaseModel):
    name: str
    t: int
    v: float


class Statistics(BaseModel):
    avg: float
    sum: float
