from os import path
from celery import Celery
from django.conf import settings
from docker.errors import APIError
from .client import DockerClient


app = Celery(
    'dockerboard', 
    backend='redis://localhost',
    broker='redis://localhost',
)


@app.task(name='restart_container')
def restart_container(container_id, *args, **kwargs):
    try:
        client = DockerClient()
        container = client.get_container(container_id)
        container.restart()
    except APIError as e:
        return False
    return True


@app.task(name='stop_container')
def stop_container(container_id, *args, **kwargs):
    try:
        client = DockerClient()
        container = client.get_container(container_id)
        container.stop()
    except APIError as e:
        return False
    return True


@app.task(name='start_container')
def start_containers(container_id, *args, **kwargs):
    try:
        client = DockerClient()
        container = client.get_container(container_id)
        container.start()
    except APIError as e:
        return False
    return True
