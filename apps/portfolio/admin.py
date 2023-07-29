from django.contrib import admin

from .models import Project, Tag, Skill, Contact, AboutMe, Service


# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created', 'updated')
    search_fields = ('title', 'description')
    list_filter = ('created', 'updated')


admin.site.register(Project)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated')
    search_fields = ('name',)
    list_filter = ('created', 'updated')


admin.site.register(Tag)


class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated')
    search_fields = ('name',)
    list_filter = ('created', 'updated')


admin.site.register(Skill)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated')
    search_fields = ('name',)
    list_filter = ('created', 'updated')


admin.site.register(Contact)


class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated')
    search_fields = ('name',)
    list_filter = ('created', 'updated')


admin.site.register(AboutMe)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'created', 'updated')
    search_fields = ('name',)
    list_filter = ('created', 'updated')


admin.site.register(Service)
