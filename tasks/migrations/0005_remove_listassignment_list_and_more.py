# Generated by Django 4.0.4 on 2022-06-09 12:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0004_alter_task_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listassignment',
            name='list',
        ),
        migrations.RemoveField(
            model_name='listassignment',
            name='task',
        ),
        migrations.RemoveField(
            model_name='listassignment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='task',
            name='assigned',
        ),
        migrations.DeleteModel(
            name='Assignment',
        ),
        migrations.DeleteModel(
            name='ListAssignment',
        ),
    ]
