# Generated by Django 5.0.6 on 2024-05-20 13:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_kullanici_dogum_gunu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='kullanici',
            name='dogum_gunu',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 20, 0, 0)),
        ),
    ]