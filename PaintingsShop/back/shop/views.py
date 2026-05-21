from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Picture, About
from .serializers import PictureSerializer, AboutSerializer


class PictureViewSet(ModelViewSet):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer


class AboutViewSet(ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer