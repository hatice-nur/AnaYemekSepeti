# Generated by Django 5.0.6 on 2024-05-20 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('YemekSepeti', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siparis',
            name='tutar',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='siparisdetay',
            name='fiyat',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='siparisdetay',
            name='toplam_tutar',
            field=models.FloatField(),
        ),
    ]
