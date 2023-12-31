FROM python:3.9

WORKDIR /app

COPY ./requirements.txt .

RUN pip install --upgrade pip
RUN pip install --no-cache-dir  -r requirements.txt

COPY . /app

EXPOSE 8090
WORKDIR /app/src
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8090"]