from django.http import HttpResponse, HttpResponseNotModified
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers

from .client import DockerClient
from .serializers import ContainerSerializer


class ContainerList(APIView):
    """
    List all containers or add a new snippet.
    """
    def get(self, request, format=None):
        client = DockerClient()
        serializer = ContainerSerializer(client.list_containers(), many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SnippetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ContainerView(APIView):
    """
    Retrieve, update or delete a container instance.
    """
    def get(self, request, pk, format=None):
        container = None
        serializer = ContainerSerializer(snippet)
        return Response(serializer.data)

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

