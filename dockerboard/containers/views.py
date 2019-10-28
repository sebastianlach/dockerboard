from django.shortcuts import render
from datasource.source import DockerSource


def list(request):
    datasource = DockerSource()
    context = dict(
        containers=datasource.containers(all=True),
    )
    return render(request, 'containers/list.html', context)
