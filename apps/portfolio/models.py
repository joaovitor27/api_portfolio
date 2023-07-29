from django.db import models
from django.utils.translation import gettext_lazy as _


class Tag(models.Model):
    name = models.CharField(verbose_name=_('Nome'), max_length=100)
    icons = models.CharField(verbose_name=_('Ícone'), max_length=100, blank=True, null=True)
    created = models.DateTimeField(verbose_name=_('Criado em'), auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_('Atualizado em'), auto_now=True)

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')
        ordering = ['name']

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(verbose_name=_('Título'), max_length=100)
    description = models.TextField(verbose_name=_('Descrição'))
    image = models.ImageField(verbose_name=_('Imagem'), upload_to='projects', blank=True, null=True)
    tags = models.ManyToManyField(Tag, verbose_name=_('Tags'), blank=True)
    url_project = models.URLField(verbose_name=_('URL Project'), blank=True, null=True)
    url_github = models.URLField(verbose_name=_('URL Github'), blank=True, null=True)
    created = models.DateTimeField(verbose_name=_('Criado em'), auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_('Atualizado em'), auto_now=True)

    class Meta:
        verbose_name = _('Projeto')
        verbose_name_plural = _('Projetos')
        ordering = ['-created']

    def __str__(self):
        return self.title


class Skill(models.Model):
    CHOICES_LEVEL = (
        ('B', _('Básico')),
        ('I', _('Intermediário')),
        ('A', _('Avançado')),
        ('E', _('Expert')),
    )

    name = models.CharField(verbose_name=_('Nome'), max_length=100)
    image = models.ImageField(verbose_name=_('Imagem'), upload_to='skills', blank=True, null=True)
    percentage = models.DecimalField(verbose_name=_('Porcentagem'), max_digits=5, decimal_places=2)
    level = models.CharField(verbose_name=_('Nível'), max_length=1, choices=CHOICES_LEVEL, default='B')
    created = models.DateTimeField(verbose_name=_('Criado em'), auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_('Atualizado em'), auto_now=True)

    class Meta:
        verbose_name = _('Skill')
        verbose_name_plural = _('Skills')
        ordering = ['-created']

    def __str__(self):
        return self.name


class AboutMe(models.Model):
    name = models.CharField(verbose_name=_('Nome'), max_length=100)
    description = models.TextField(verbose_name=_('Descrição'))
    image = models.ImageField(verbose_name=_('Imagem'), upload_to='aboutme', blank=True, null=True)
    email = models.EmailField(verbose_name=_('Email'))
    address = models.CharField(verbose_name=_('Endereço'), max_length=200)
    phone = models.CharField(verbose_name=_('Telefone'), max_length=14)
    skills = models.ManyToManyField(Skill, verbose_name=_('Skills'), blank=True)
    url_site = models.URLField(verbose_name=_('URL Site'), blank=True, null=True)
    url_linkedin = models.URLField(verbose_name=_('URL Linkedin'), blank=True, null=True)
    url_github = models.URLField(verbose_name=_('URL Github'), blank=True, null=True)
    url_instagram = models.URLField(verbose_name=_('URL Instagram'), blank=True, null=True)
    url_facebook = models.URLField(verbose_name=_('URL Facebook'), blank=True, null=True)
    url_twitter = models.URLField(verbose_name=_('URL Twitter'), blank=True, null=True)
    url_youtube = models.URLField(verbose_name=_('URL Youtube'), blank=True, null=True)
    url_whatsapp = models.CharField(verbose_name=_('URL Whatsapp'), max_length=20, blank=True, null=True)
    url_telegram = models.CharField(verbose_name=_('URL Telegram'), max_length=20, blank=True, null=True)

    class Meta:
        verbose_name = _('Sobre mim')
        verbose_name_plural = _('Sobre mim')

    def __str__(self):
        return self.name


class Service(models.Model):
    title = models.CharField(verbose_name=_('Título'), max_length=200)
    description = models.TextField(verbose_name=_('Descrição'))
    image = models.ImageField(verbose_name=_('Imagem'), upload_to='services', blank=True, null=True)
    url = models.URLField(verbose_name=_('URL'), blank=True, null=True)
    created = models.DateTimeField(verbose_name=_('Criado em'), auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_('Atualizado em'), auto_now=True)

    class Meta:
        verbose_name = _('Serviço')
        verbose_name_plural = _('Serviços')
        ordering = ['-created']

    def __str__(self):
        return self.title


class Contact(models.Model):
    CHOICES_PROGRESS = (
        (0, _('Não iniciado')),
        (1, _('Em andamento')),
        (2, _('Finalizado')),
    )

    name = models.CharField(verbose_name=_('Nome'), max_length=120)
    email = models.EmailField(verbose_name=_('Email'))
    subject = models.CharField(verbose_name=_('Assunto'), max_length=150)
    message = models.TextField(verbose_name=_('Mensagem'))
    created = models.DateTimeField(verbose_name=_('Criado em'), auto_now_add=True)
    updated = models.DateTimeField(verbose_name=_('Atualizado em'), auto_now=True)
    progress = models.IntegerField(verbose_name=_('Progresso'), default=0, choices=CHOICES_PROGRESS)
    active = models.BooleanField(verbose_name=_('Ativo'), default=True)

    class Meta:
        verbose_name = _('Contato')
        verbose_name_plural = _('Contatos')
        ordering = ['created']

    def __str__(self):
        return self.name
