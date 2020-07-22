from django.shortcuts import render


def list(request):
    context = dict(
        images=client.images(),
    )
    return render(request, 'images/list.html', context)


def details(request, image_id):
    context = dict(
        image=client.get_image(image_id),
    )
    return render(request, 'images/details.html', context)


