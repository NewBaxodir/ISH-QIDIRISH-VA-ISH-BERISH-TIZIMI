# Generated by Django 2.2.3 on 2021-04-30 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='vacanciess',
            options={'verbose_name': "E'LON ISH O'RNI", 'verbose_name_plural': "E'LON ISH O'RNI"},
        ),
        migrations.RemoveField(
            model_name='vacanciess',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='vacanciess',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='vacanciess',
            name='phone_name',
        ),
    ]
