class DockerizeImage(object):

    image = None

    def __init__(self, image):
        self.image = image

    @property
    def id(self):
        return self.image.id

    @property
    def name(self):
        return self.image.short_id.split(':')[1][:8]

    @property
    def tags(self):
        return self.image.tags

    @property
    def tags_short(self):
        return "; ".join(self.image.tags)[:40]

    def __str__(self):
        return 'Image <{}>'.format(self.image.id)

