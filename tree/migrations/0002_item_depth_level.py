# Generated by Django 3.0.2 on 2020-01-26 17:01

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='depth_level',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(-1)], verbose_name='Уровень'),
            preserve_default=False,
        ),
    ]
