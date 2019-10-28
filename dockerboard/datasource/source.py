from docker import from_env


class DockerSource(object):

    def __init__(self, url=None):
        self.client = from_env()

    def containers(self, *args, **kwargs):
        return self.client.containers.list(**kwargs)

    def images(self, *args, **kwargs):
        return self.client.images.list(**kwargs)
