from celery import Celery

# # 开启Django支持
# import os
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_practice.settings')
# import django
# django.setup()


# 实例化celery对象
app = Celery('test')
app.config_from_object('celery_proj.celeryconfig')