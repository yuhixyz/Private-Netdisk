# Generated by Django 3.1.5 on 2021-01-28 11:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20210128_1955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='bucket',
        ),
        migrations.RemoveField(
            model_name='myuser',
            name='region',
        ),
    ]