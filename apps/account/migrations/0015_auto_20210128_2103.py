# Generated by Django 3.1.5 on 2021-01-28 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_auto_20210128_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='bucket',
            field=models.CharField(default='1304853137', max_length=127),
        ),
        migrations.AddField(
            model_name='myuser',
            name='region',
            field=models.CharField(default='ap-nanjing', max_length=32),
        ),
    ]
