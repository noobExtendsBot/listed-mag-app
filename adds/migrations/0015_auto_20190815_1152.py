# Generated by Django 2.2.3 on 2019-08-15 11:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('adds', '0014_auto_20190814_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 15, 11, 52, 13, 469976, tzinfo=utc)),
        ),
    ]