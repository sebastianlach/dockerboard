from django.shortcuts import render
from dockerize.client import DockerizeClient


def list(request):
    client = DockerizeClient()
    context = dict(
        containers=client.containers(all=True),
    )
    return render(request, 'containers/list.html', context)


def details(request, container_id):
    client = DockerizeClient()
    context = dict(
        container=client.get_container(container_id)
    )
    return render(request, 'containers/details.html', context)

