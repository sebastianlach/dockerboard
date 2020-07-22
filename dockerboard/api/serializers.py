from rest_framework import serializers


class ContainerImageSerializer(serializers.Serializer):
    tags = serializers.CharField(read_only=True)


class ContainerSerializer(serializers.Serializer):
    image = ContainerImageSerializer()
