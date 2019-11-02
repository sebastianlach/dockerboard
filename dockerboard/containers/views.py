from django.http import HttpResponse, HttpResponseNotModified
from django.shortcuts import render
from dockerize.client import DockerizeClient
from dockerize.tasks import app


def list(request):
    client = DockerizeClient()
    containers = client.containers(all=True)
    context = dict(
        containers=containers,
    )
    return render(request, 'containers/list.html', context)


def details(request, container_id):
    client = DockerizeClient()
    context = dict(
        container=client.get_container(container_id)
    )
    return render(request, 'containers/details.html', context)


def start(request, container_id):
    task = app.send_task('start_container', [container_id,])
    result = task.get(timeout=60)
    return HttpResponse() if result else HttpResponseNotModified()


def restart(request, container_id):
    task = app.send_task('restart_container', [container_id,])
    result = task.get(timeout=60)
    return HttpResponse() if result else HttpResponseNotModified()


def stop(request, container_id):
    task = app.send_task('stop_container', [container_id,])
    result = task.get(timeout=60)
    return HttpResponse() if result else HttpResponseNotModified()

