from django.db import models
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet


class File(models.Model):

    file = models.FileField()


class FileSerializer(ModelSerializer):

    class Meta:
        model = File
        fields = '__all__'


class FileViewSet(ModelViewSet):

    queryset = File.objects.all()
    serializer_class = FileSerializer
