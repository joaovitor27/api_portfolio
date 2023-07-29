from django.urls import path, include
from rest_framework import routers

from . import views

app_name = 'portfolio'

router = routers.DefaultRouter()
router.register('project', views.ProjectViewSet, basename='project')
router.register('tag', views.TagViewSet, basename='tag')
router.register('skill', views.SkillViewSet, basename='skill')
router.register('contact-form', views.ContactViewSet, basename='contact-from')
router.register('contact', views.ContactGerenicViewSet, basename='contact')


urlpatterns = [
    path('', include(router.urls)),
]
