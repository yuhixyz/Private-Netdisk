# Generated by Django 3.1.5 on 2021-01-28 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='bucket',
            field=models.CharField(default='test_buckey', max_length=128),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='myuser',
            name='region',
            field=models.CharField(default='ap-nanjing', max_length=32),
            preserve_default=False,
        ),
    ]
