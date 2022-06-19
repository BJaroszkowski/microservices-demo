FROM python:3.10

WORKDIR /api

COPY requirements.txt /api/
RUN pip install -r requirements.txt --no-cache-dir

COPY ./src /api

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
