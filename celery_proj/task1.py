# 任务源
from . import app

@app.task
def add(num1, num2):
    res = num1 + num2
    print(res)
    return res