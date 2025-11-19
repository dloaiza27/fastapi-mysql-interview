from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from app.core.database import engine

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, nullable=False)
    name = Column(String(255))
Base.metadata.create_all(bind=engine)
