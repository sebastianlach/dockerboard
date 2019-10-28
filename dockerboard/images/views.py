from django.shortcuts import render
from datasource.source import DockerSource


def list(request):
    datasource = DockerSource()
    context = dict(
        images=datasource.images,
    )
    return render(request, 'images/list.html', context)
