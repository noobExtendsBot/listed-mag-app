# Generated by Django 2.2.3 on 2019-08-20 20:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20190820_2029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='is_active',
        ),
    ]
