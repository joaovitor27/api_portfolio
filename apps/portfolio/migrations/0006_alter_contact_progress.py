# Generated by Django 4.2.3 on 2023-07-27 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_alter_skill_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='progress',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5, verbose_name='Progresso'),
        ),
    ]