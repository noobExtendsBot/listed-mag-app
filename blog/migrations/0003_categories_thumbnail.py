# Generated by Django 2.2.3 on 2019-08-12 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='thumbnail',
            field=models.ImageField(default='none', upload_to='posts/categories/thumbnails/'),
        ),
    ]
