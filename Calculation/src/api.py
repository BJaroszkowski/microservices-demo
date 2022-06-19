import statistics
from http import HTTPStatus

from fastapi import APIRouter

router = APIRouter()


@router.post("/", status_code=HTTPStatus.OK)
async def calculate_statistics(results: list[float]):
    return {"avg": statistics.mean(results), "sum": sum(results)}
