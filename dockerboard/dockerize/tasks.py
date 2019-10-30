from os import path
from celery import Celery
from django.conf import settings
from docker.errors import APIError
from .client import DockerizeClient


app = Celery(
    'dockerize', 
    backend='redis://localhost',
    broker='redis://localhost',
)


@app.task(name='restart_container')
def restart_containers(container_id, *args, **kwargs):
    try:
        client = DockerizeClient()
        container = client.get_container(container_id)
        container.restart()
    except APIError as e:
        return False
    return True
