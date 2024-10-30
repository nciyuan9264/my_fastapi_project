from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from blog.app import crud
from blog.app.api import deps

router = APIRouter()


@router.get("/")
def read_users(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100,
):
    users = crud.user.get_multi(db, skip=skip, limit=limit)
    return users
