# Generated by Django 5.1.1 on 2024-09-16 15:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_foodentry_delete_moodentry'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodentry',
            name='quantity',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]
