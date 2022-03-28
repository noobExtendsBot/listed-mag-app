# Generated by Django 2.2.3 on 2019-08-11 10:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('adds', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='add',
            name='title',
            field=models.CharField(default='no title', max_length=100),
        ),
        migrations.AlterField(
            model_name='add',
            name='published_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 11, 10, 58, 28, 69675, tzinfo=utc)),
        ),
    ]
