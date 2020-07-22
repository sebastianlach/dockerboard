from rest_framework import serializers


class ImageSerializer(serializers.Serializer):
    id = serializers.CharField()
    short_id = serializers.CharField()
    tags = serializers.CharField(read_only=True)
    attrs = serializers.CharField()


class ContainerSerializer(serializers.Serializer):
    id = serializers.CharField()
    short_id = serializers.CharField()
    name = serializers.CharField()
    status = serializers.CharField()
    image = ImageSerializer()
    attrs = serializers.CharField()
