# Generated by Django 4.1.3 on 2024-05-07 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Kullanici',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]