# Generated by Django 5.0.1 on 2024-02-10 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='completed',
            field=models.BooleanField(default=False, verbose_name='Completada'),
        ),
        migrations.AlterField(
            model_name='task',
            name='description',
            field=models.TextField(blank=True, max_length=250, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='task',
            name='title',
            field=models.CharField(blank=True, max_length=25, verbose_name='Título'),
        ),
    ]
