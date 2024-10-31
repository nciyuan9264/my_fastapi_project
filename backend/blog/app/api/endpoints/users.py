from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from blog.app import crud
from blog.app.api import deps
from blog.app.worker import add, celery_app  # 引入celery实例

router = APIRouter()

# 触发任务
@router.get("/")
def read_users(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100,
):
    # 异步触发任务
    res = add.delay(10000)
    return {"task_id": res.id, "status": res.status}

# 查询任务状态
@router.get("/task_status/{task_id}")
def get_task_status(task_id: str):
    result = celery_app.AsyncResult(task_id)
    return {"task_id": task_id, "status": result.status, "result": result.result}
