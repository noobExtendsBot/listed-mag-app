# Generated by Django 2.2.3 on 2019-08-20 20:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('adds', '0026_auto_20190820_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 20, 20, 28, 41, 58388, tzinfo=utc)),
        ),
    ]
