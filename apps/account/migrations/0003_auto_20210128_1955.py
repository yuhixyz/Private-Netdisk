# Generated by Django 3.1.5 on 2021-01-28 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20210128_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='bucket',
            field=models.CharField(default='test4aliyun-1304853137', max_length=127),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='region',
            field=models.CharField(default='ap-nanjing', max_length=32),
        ),
    ]
