FROM python:3.12

WORKDIR /backend/

COPY . /backend

# 设置 PYTHONPATH
ENV PYTHONPATH=/backend

RUN pip install poetry #--no-cache-dir

COPY pyproject.toml poetry.lock* /backend/

RUN poetry install # --no-root --no-dev

CMD ["poetry", "run", "uvicorn", "blog.app.main:app", "--host", "0.0.0.0", "--port", "8000"]
