# Generated by Django 4.2.3 on 2023-07-27 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_aboutme_skills_alter_project_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='active',
            field=models.BooleanField(default=True, verbose_name='Ativo'),
        ),
        migrations.AddField(
            model_name='contact',
            name='progress',
            field=models.IntegerField(default=0, verbose_name='Progresso'),
        ),
        migrations.AddField(
            model_name='contact',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Atualizado em'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='icons',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Ícone'),
        ),
    ]
