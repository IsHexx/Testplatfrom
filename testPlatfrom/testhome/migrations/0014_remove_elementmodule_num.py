# Generated by Django 3.1.3 on 2022-11-25 06:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testhome', '0013_auto_20221122_1154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='elementmodule',
            name='num',
        ),
    ]
