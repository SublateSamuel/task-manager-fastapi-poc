from sqlalchemy.orm import Session
from database.database import SessionLocal
from models.task import Task
from schemas.task import Task as TaskSchema

def get_db():
  db = SessionLocal()
  try:
    yield db
  finally:
    db.close()

def create_new_task(db: Session, task: TaskSchema):
    db_task= Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks(db: Session, skip: int = 0, limit: int = 100):
  return db.query(Task).offset(skip).limit(limit).all()

def get_first_task(db: Session):
  return db.query(Task).first()