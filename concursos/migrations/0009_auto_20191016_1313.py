# Generated by Django 2.2.6 on 2019-10-16 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('concursos', '0008_auto_20191016_1000'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='llamado',
            name='es_concurso_publico',
        ),
        migrations.RemoveField(
            model_name='llamado',
            name='es_revalida',
        ),
        migrations.AlterField(
            model_name='llamado',
            name='is_public',
            field=models.BooleanField(default=False, verbose_name='Publicado'),
        ),
    ]
