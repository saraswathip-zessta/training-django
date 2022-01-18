# Generated by Django 3.2.11 on 2022-01-17 10:42

from django.db import migrations
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('asset_tracker', '0005_alter_employeeskills_frontend_tech_stack'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeskills',
            name='frontend_tech_stack',
            field=smart_selects.db_fields.ChainedManyToManyField(chained_field='skill_type', chained_model_field='name', horizontal=True, related_name='employee_frontend_skills', to='asset_tracker.Skills'),
        ),
    ]
