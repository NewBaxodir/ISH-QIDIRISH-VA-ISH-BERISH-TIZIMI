# Generated by Django 2.2.3 on 2021-04-26 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_user_username'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
