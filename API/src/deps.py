from typing import Any, Iterator

import requests
from config import Settings
from pydantic import SecretStr
from retry import retry
from schemas import Result, Statistics
from sqlalchemy import create_engine

# TODO: given the data structure at the moment, in a production environment it
# would be probably a better idea to use non-relational db like MongoDB
from sqlalchemy.orm import Session, sessionmaker

settings = Settings()


def prepare_database(database: SecretStr):
    engine = create_engine(
        database.get_secret_value(),
    )
    return engine


engine = prepare_database(settings.database)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db() -> Iterator[Session]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class CalculationClient:
    def __init__(self, api_url: str) -> None:
        self.api_url = api_url + "/api/"

    # TODO: limit retries to connection errors and return error code when connection fails
    @retry(tries=5, backoff=2)
    def _get(self, url: str, data: dict[str, Any] | None):
        resp = requests.get(url, json=data)
        resp.raise_for_status()
        return resp.json()

    def get_statistics(self, results: list[Result]) -> Statistics:
        data = [result.value for result in results]
        json_response = self._get(url=self.api_url, data=data)
        return Statistics.parse_obj(json_response)


def get_calculation_client():
    return CalculationClient(settings.calculator_url)
