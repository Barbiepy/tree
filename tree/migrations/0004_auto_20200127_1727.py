# Generated by Django 3.0.2 on 2020-01-27 17:27

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('tree', '0003_auto_20200126_1701'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='item',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]