# Generated by Django 2.2.3 on 2021-05-01 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summary', '0019_auto_20210501_1226'),
    ]

    operations = [
        migrations.AddField(
            model_name='summary',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='summary',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='summary',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='summary',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='summary',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='summary',
            name='image6',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
