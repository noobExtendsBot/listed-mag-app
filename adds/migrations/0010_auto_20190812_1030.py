# Generated by Django 2.2.3 on 2019-08-12 10:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('adds', '0009_auto_20190812_1030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 12, 10, 30, 59, 48425, tzinfo=utc)),
        ),
    ]
