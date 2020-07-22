from rest_framework import serializers


class ContainerImageSerializer(serializers.Serializer):
    tags = serializers.CharField(read_only=True)


class ContainerSerializer(serializers.Serializer):
    id = serializers.CharField()
    short_id = serializers.CharField()
    name = serializers.CharField()
    status = serializers.CharField()
    image = ContainerImageSerializer()
    attrs = serializers.CharField()
