# Generated by Django 5.0.1 on 2024-02-10 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_alter_task_completed_alter_task_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
