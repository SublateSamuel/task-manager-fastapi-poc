from sqlalchemy import Column, Integer, String
from database.database import Base

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    surname = Column(String)
    repetitions = Column(Integer)
