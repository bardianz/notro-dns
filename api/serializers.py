from rest_framework import serializers


class ServiceSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200)
    prefred_ip = serializers.CharField(max_length=15)
    alternate_ip = serializers.CharField(max_length=15)
