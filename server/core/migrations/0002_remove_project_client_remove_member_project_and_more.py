# Generated by Django 5.0.3 on 2024-04-18 11:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='client',
        ),
        migrations.RemoveField(
            model_name='member',
            name='project',
        ),
        migrations.RemoveField(
            model_name='timesheet',
            name='project',
        ),
        migrations.RemoveField(
            model_name='timesheet',
            name='user',
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='Member',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='TimeSheet',
        ),
    ]