from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from blog.app.core.config import settings
# print('666', settings.SQLALCHEMY_DATABASE_URI)
engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI), pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
