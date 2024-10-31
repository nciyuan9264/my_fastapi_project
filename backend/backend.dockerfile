FROM python:3.12

WORKDIR /backend/

COPY . /backend

# 设置 PYTHONPATH
ENV PYTHONPATH=/backend

RUN pip install poetry

COPY pyproject.toml poetry.lock* /backend/

# RUN poetry install --no-root --no-dev
RUN poetry install --no-root --no-dev && \
    ln -s $(poetry env info --path)/bin/celery /usr/local/bin/celery
# 复制启动脚本并赋予可执行权限
RUN chmod +x /backend/blog/start.sh

# 启动脚本
CMD ["/backend/blog/start.sh"]
