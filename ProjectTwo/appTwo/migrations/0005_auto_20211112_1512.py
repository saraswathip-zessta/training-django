# Generated by Django 3.1.13 on 2021-11-12 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appTwo', '0004_auto_20211112_1226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itemslist',
            name='id',
        ),
        migrations.AlterField(
            model_name='itemslist',
            name='item_name',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]
