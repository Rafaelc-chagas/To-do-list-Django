from django.db import models


class Task(models.Model):
    title = models.CharField(blank=True, max_length=25, verbose_name='Título')
    description = models.TextField(blank=True, max_length=250, verbose_name='Descrição')
    completed = models.BooleanField(default=False, verbose_name='Completada')
    datetime = models.DateTimeField(auto_now=True)
