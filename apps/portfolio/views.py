from rest_framework import viewsets

from .models import Project, Tag, Skill, Contact, AboutMe, Service
from .serializer import (ProjectSerializer, TagSerializer, SkillSerializer, ContactSerializer, AboutMeSerializer,
                         ServiceSerializer, ContactGerenicSerializer)


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']


class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer
    http_method_names = ['get', 'post', 'put', 'patch', 'delete']


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.filter(active=True)
    serializer_class = ContactSerializer
    http_method_names = ['post']


class ContactGerenicViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactGerenicSerializer
    http_method_names = ['get', 'patch', 'delete']


class AboutMeViewSet(viewsets.ModelViewSet):
    queryset = AboutMe.objects.all()
    serializer_class = AboutMeSerializer
    http_method_names = ['get', 'post', 'put', 'patch']


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
