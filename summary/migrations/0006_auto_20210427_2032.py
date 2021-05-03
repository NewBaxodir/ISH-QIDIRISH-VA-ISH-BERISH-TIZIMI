# Generated by Django 2.2.3 on 2021-04-27 17:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('summary', '0005_auto_20210427_1851'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workexperience',
            name='begwork',
        ),
        migrations.RemoveField(
            model_name='workexperience',
            name='finishw',
        ),
        migrations.RemoveField(
            model_name='workexperience',
            name='organiza',
        ),
        migrations.RemoveField(
            model_name='workexperience',
            name='position',
        ),
        migrations.RemoveField(
            model_name='workexperience',
            name='workplaceres',
        ),
        migrations.AddField(
            model_name='workexperience',
            name='class_name',
            field=models.CharField(default=datetime.datetime(2021, 4, 27, 17, 32, 30, 956419, tzinfo=utc), max_length=32),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workexperience',
            name='english',
            field=models.CharField(default=datetime.datetime(2021, 4, 27, 17, 32, 33, 820066, tzinfo=utc), max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workexperience',
            name='nepali',
            field=models.CharField(default=datetime.datetime(2021, 4, 27, 17, 32, 36, 886336, tzinfo=utc), max_length=3),
            preserve_default=False,
        ),
    ]
