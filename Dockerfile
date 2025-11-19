FROM python:3.11

WORKDIR /workspace

COPY requirements.txt .

RUN apt-get update && apt-get install -y build-essential libssl-dev libffi-dev python3-dev

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install cryptography pymysql

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
