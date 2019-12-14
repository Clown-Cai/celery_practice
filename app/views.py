from django.shortcuts import render, HttpResponse

# from celery_proj import task1
from app import task

def test(request):
    res = task.add.delay(30,23)
    print(res)  # 任务ID
    # task.add.apply_async(args=(30,20), countdown=40)
    return HttpResponse('hello')
