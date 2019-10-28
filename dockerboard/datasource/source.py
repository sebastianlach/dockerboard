from docker import from_env


class DockerSource(object):

    def __init__(self, url=None):
        self.client = from_env()

    @property
    def containers(self):
        return self.client.containers.list()

    @property
    def images(self):
        return self.client.images.list()
