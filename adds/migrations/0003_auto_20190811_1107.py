# Generated by Django 2.2.3 on 2019-08-11 11:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('adds', '0002_auto_20190811_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add',
            name='priority',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='add',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 11, 11, 7, 5, 694576, tzinfo=utc)),
        ),
    ]
