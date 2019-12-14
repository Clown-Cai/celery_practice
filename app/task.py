from celery_proj import app
from celery import shared_task

# @shared_task
@app.task
def add(a,b):
    print(a+b)
    return a+b