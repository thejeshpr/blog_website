# Generated by Django 2.1.5 on 2019-01-23 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_auto_20190123_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='img',
            field=models.URLField(blank=True),
        ),
    ]
