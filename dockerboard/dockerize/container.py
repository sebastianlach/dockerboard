from dockerize.image import DockerizeImage


class DockerizeContainer(object):

    container = None
    attrs = dict()

    def __init__(self, container):
        self.container = container
        self.attrs = container.attrs

    @property
    def id(self):
        return self.container.id

    @property
    def name(self):
        return self.container.name

    @property
    def image(self):
        return DockerizeImage(self.container.image)

    @property
    def status(self):
        return self.container.status

    def __str__(self):
        return 'Container <{}>'.format(self.id)

