from docker import from_env


class DockerClient(object):

    def __init__(self, url=None):
        self.client = from_env()

    def list_containers(self, *args, **kwargs):
        return self.client.containers.list(**kwargs)

    def get_container(self, container_id, *args, **kwargs):
        return self.client.containers.get(container_id)

    def list_images(self, *args, **kwargs):
        return self.client.images.list(**kwargs)

    def get_image(self, image_id, *args, **kwargs):
        return self.client.images.get(image_id)
