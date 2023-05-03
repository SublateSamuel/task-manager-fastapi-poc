from fastapi import Depends, FastAPI
from typing import List, Optional
from schemas.task import Task
from sqlalchemy.orm import Session
from worker import process_task
from database import repository
from database.database import engine, Base
from fastapi.responses import RedirectResponse


Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.get("/")
async def read_root():
    '''Home da aplicação'''
    return RedirectResponse(url='/docs')

@app.get('/tasks')
async def read_form(db: Session = Depends(repository.get_db)) -> List[Optional[Task]]:
    '''Lista tarefas criadas'''
    return repository.get_tasks(db)

@app.post('/task', status_code=201, response_model=Task)
async def create_task(task: Task, db: Session = Depends(repository.get_db)) -> Task:
    '''Cria novas tarefas'''
    repository.create_new_task(db, task)
    task_id = process_task.delay(task.dict()).id
    print(task.dict())
    print(task_id)
    return task
