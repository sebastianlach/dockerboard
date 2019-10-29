from django.shortcuts import render
from dockerize.client import DockerizeClient


def list(request):
    client = DockerizeClient()
    context = dict(
        images=client.images(),
    )
    return render(request, 'images/list.html', context)


def details(request, image_id):
    client = DockerizeClient()
    context = dict(
        image=client.get_image(image_id),
    )
    return render(request, 'images/details.html', context)


