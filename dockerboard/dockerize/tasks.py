from os import path
from celery import Celery
from django.conf import settings


app = Celery(
    'dockerize', 
    backend='redis://localhost',
    broker='redis://localhost',
)


@app.task(name='sample')
def restart_containers(*args, **kwargs):
    return sum(args)

