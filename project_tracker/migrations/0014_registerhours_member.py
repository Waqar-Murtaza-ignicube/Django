# Generated by Django 4.2.11 on 2024-03-20 06:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project_tracker', '0013_remove_registerhours_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='registerhours',
            name='member',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='project_tracker.member'),
        ),
    ]
