# Generated by Django 3.1.3 on 2022-10-12 02:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testhome', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='data_date',
            field=models.CharField(max_length=20),
        ),
    ]
