# Generated by Django 4.2.11 on 2024-03-25 07:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_tracker', '0026_remove_member_company_alter_member_project_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='project_deadline',
            field=models.DateField(default=datetime.datetime(2024, 3, 25, 7, 31, 57, 891774)),
        ),
        migrations.AlterField(
            model_name='registerhours',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 3, 25, 7, 31, 57, 892612)),
        ),
    ]
