from django.shortcuts import render
from datasource.source import DockerSource


def list(request):
    datasource = DockerSource()
    images = datasource.images
    context = dict(
        images=images,
        count=len(images),
    )
    return render(request, 'images/list.html', context)
