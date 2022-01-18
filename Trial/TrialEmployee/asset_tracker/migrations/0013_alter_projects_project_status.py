# Generated by Django 3.2.11 on 2022-01-18 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('asset_tracker', '0012_projects_project_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='project_status',
            field=models.CharField(blank=True, choices=[('New', 'New'), ('Open', 'Available'), ('In Progress', 'In Progress'), ('Completed', 'Completed')], max_length=50),
        ),
    ]
