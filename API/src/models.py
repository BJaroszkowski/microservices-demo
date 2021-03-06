from sqlalchemy import BigInteger, Column, Float, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Result(Base):
    __tablename__ = "results"

    id = Column(Integer, primary_key=True)
    data_point = Column(String(255), nullable=False)
    timestamp = Column(BigInteger, nullable=False)
    value = Column(Float, nullable=True)
