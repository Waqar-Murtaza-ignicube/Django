# Generated by Django 4.2.11 on 2024-03-25 07:06

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_tracker', '0025_alter_client_company_alter_project_project_deadline_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='company',
        ),
        migrations.AlterField(
            model_name='member',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='project_tracker.project'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_deadline',
            field=models.DateField(default=datetime.datetime(2024, 3, 25, 7, 6, 29, 779672)),
        ),
        migrations.AlterField(
            model_name='registerhours',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 3, 25, 7, 6, 29, 780135)),
        ),
    ]
