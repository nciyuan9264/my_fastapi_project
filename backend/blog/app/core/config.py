from typing import Any, Dict, Optional, List
from pydantic import AnyUrl, field_validator, AnyHttpUrl
from pydantic_core.core_schema import ValidationInfo
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_HOST: str
    MYSQL_DATABASE: str
    SQLALCHEMY_DATABASE_URI: Optional[AnyUrl] = None
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = ['http://localhost:5173']

    @field_validator("SQLALCHEMY_DATABASE_URI", mode='before')
    @classmethod
    def assemble_db_connection(cls, v: Optional[str], info) -> Any:
        if isinstance(v, str):
            return v

        # 使用 info.data 来访问其他字段的值
        return f'mysql+pymysql://{info.data["MYSQL_USER"]}:{info.data["MYSQL_PASSWORD"]}@{info.data["MYSQL_HOST"]}/{info.data["MYSQL_DATABASE"]}'

    class Config:
        case_sensitive = True

    def check_env_variables(self):
        print("Loaded Environment Variables:")
        print(f"MYSQL_USER: {self.MYSQL_USER}")
        print(f"MYSQL_PASSWORD: {self.MYSQL_PASSWORD}")
        print(f"MYSQL_HOST: {self.MYSQL_HOST}")
        print(f"MYSQL_DATABASE: {self.MYSQL_DATABASE}")
        print(f"SQLALCHEMY_DATABASE_URI: {self.SQLALCHEMY_DATABASE_URI}")

# 实例化 Settings
settings = Settings()
settings.check_env_variables()