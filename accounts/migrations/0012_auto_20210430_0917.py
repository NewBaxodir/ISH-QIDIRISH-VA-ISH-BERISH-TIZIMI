# Generated by Django 2.2.3 on 2021-04-30 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0011_auto_20210429_1008'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': '1. UMUMIY FOYDALANUVCHILAR BAZASI', 'verbose_name_plural': '1. UMUMIY FOYDALANUVCHILAR BAZASI'},
        ),
        migrations.AlterModelOptions(
            name='vacancies',
            options={'verbose_name': '2. ISH BERUVCHI FOYDALANUVCHILAR BAZASI', 'verbose_name_plural': '2. ISH BERUVCHI FOYDALANUVCHILAR BAZASI'},
        ),
    ]