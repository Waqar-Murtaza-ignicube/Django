# Generated by Django 4.2.11 on 2024-03-25 06:48

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_tracker', '0024_remove_project_company_alter_client_client_contact_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='clients', to='project_tracker.company'),
        ),
        migrations.AlterField(
            model_name='project',
            name='project_deadline',
            field=models.DateField(default=datetime.datetime(2024, 3, 25, 6, 48, 10, 434022)),
        ),
        migrations.AlterField(
            model_name='registerhours',
            name='date',
            field=models.DateField(default=datetime.datetime(2024, 3, 25, 6, 48, 10, 434503)),
        ),
    ]
