from pydantic import BaseModel


class Result(BaseModel):
    data_point: str
    timestamp: int
    value: float


class Statistics(BaseModel):
    avg: float
    sum: float
