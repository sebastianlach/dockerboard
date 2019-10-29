from django.shortcuts import render
from dockerize.client import DockerizeClient


def list(request):
    client = DockerizeClient()
    context = dict(
        images=client.images(),
    )
    return render(request, 'images/list.html', context)

