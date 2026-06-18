FROM python:3.13-slim

ENV UV_SYSTEM_PYTHON=1

WORKDIR /app

COPY . .

RUN pip install uv

RUN uv sync --no-dev

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "fastapi_zero.app:app", "--host", "0.0.0.0", "--port", "8000"]