from sqlalchemy.orm import Session

from blog.app.crud.base import CRUDBase
from blog.app.models import User

from blog.app.schemas.user import UserCreate, UserUpdate

class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def create(self, db: Session) -> str:

        return 'db_obj'

user = CRUDUser(User)