# Generated by Django 2.2.3 on 2019-08-22 18:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('adds', '0033_auto_20190820_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 22, 18, 52, 13, 537500, tzinfo=utc)),
        ),
    ]
