from pydantic import BaseModel

class Task(BaseModel):
    name: str
    surname: str
    repetitions: int

    class Config:
        orm_mode = True