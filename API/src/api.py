from http import HTTPStatus

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from schemas import Result, Statistics
from deps import get_db, get_calculation_client, CalculationClient
from models import Result as DBResult

router = APIRouter()


@router.post("/", status_code=HTTPStatus.CREATED)
async def post_result(results: list[Result], db: Session = Depends(get_db)):

    for result in results:
        db.add(result)
    db.commit()


@router.get("/health", status_code=HTTPStatus.OK)
async def healthcheck():
    return


@router.get("/{data_point}", status_code=HTTPStatus.OK, response_model=Statistics)
async def query_results(
    data_point: str,
    db: Session = Depends(get_db),
    calculation_client: CalculationClient = Depends(get_calculation_client),
    _from: int | None = Query(default=None, alias="from"),
    to: int | None = Query(default=None),
):
    query = db.query(DBResult).filter(DBResult.data_point == data_point)

    if _from is not None:
        query.filter(DBResult.timestamp >= _from)

    if to is not None:
        query.filter(DBResult.timestamp <= to)

    results = query.all()

    return calculation_client.get_statistics(results)
