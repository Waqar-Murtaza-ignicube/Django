# Generated by Django 4.2.11 on 2024-03-21 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_tracker', '0016_registerhours_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registerhours',
            old_name='date_now',
            new_name='date',
        ),
    ]