from django.shortcuts import render


def list(request):
    context = dict()
    return render(request, 'containers/list.html', context)
