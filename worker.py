from time import sleep
from celery import Celery
from schemas.task import Task

worker = Celery(broker='amqp://guest:guest@rabbitmq:5672//')

@worker.task
def process_task(task):
    print(task)
    nome = task.get('name')
    sobrenome = task.get('surname')
    repeticoes = task.get('repetitions')
    for num in range(repeticoes):
        print([f"{nome}", f"{sobrenome}", num])
        sleep(2)