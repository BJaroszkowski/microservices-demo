FROM python:3.10

WORKDIR /calculation

COPY requirements.txt /calculation/
RUN pip install -r requirements.txt --no-cache-dir

COPY ./src /calculation/

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
