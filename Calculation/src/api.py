import statistics
from http import HTTPStatus

from fastapi import APIRouter

router = APIRouter()


# TODO: depending on the size of the input we may want to make use of scipy
@router.get("/", status_code=HTTPStatus.OK)
async def calculate_statistics(results: list[float]):
    return {"avg": statistics.mean(results), "sum": sum(results)}
