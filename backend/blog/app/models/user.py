from sqlalchemy import Column, Integer, String

from blog.app.db.base_class import Base


class User(Base):
    # 这里是手动设置表名，如果不设置会自动设置为类名的小写
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), index=True)
