# Generated by Django 2.2.3 on 2021-04-28 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summary', '0011_auto_20210428_0754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workexperience',
            name='begwork',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='finishw',
            field=models.DateField(null=True),
        ),
    ]