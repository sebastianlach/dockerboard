from docker import from_env
from .container import DockerizeContainer


class DockerizeClient(object):

    def __init__(self, url=None):
        self.client = from_env()

    def containers(self, *args, **kwargs):
        return map(
            lambda container: DockerizeContainer(container),
            self.client.containers.list(**kwargs)
        )

    def get_container(self, container_id, *args, **kwargs):
        return DockerizeContainer(
            self.client.containers.get(container_id)
        )

    def images(self, *args, **kwargs):
        return self.client.images.list(**kwargs)

    def get_image(self, image_id, *args, **kwargs):
        return self.client.images.get(image_id)

