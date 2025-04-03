FROM python:3.12-slim AS builder

WORKDIR /opt/app

RUN pip install --upgrade pip wheel

COPY requirements.txt .

RUN pip wheel --no-cache-dir --wheel-dir=/opt/wheels -r requirements.txt

# -----------------------------------------------------

FROM python:3.12-slim

WORKDIR /app

COPY --from=builder /opt/wheels /wheels

RUN pip install --no-cache-dir /wheels/*

RUN rm -rf /wheels

COPY . .

EXPOSE 8080

CMD ["fastapi", "run", "main.py", "--host", "0.0.0.0", "--port", "8080"]