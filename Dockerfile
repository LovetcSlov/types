FROM python:3.12.2-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["mypy", "test_basic/", "test_intermediate/"]