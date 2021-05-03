# Generated by Django 2.2.3 on 2021-04-26 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20210426_2050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uzbekiston_provinces',
            name='region',
        ),
        migrations.CreateModel(
            name='Uzbekiston_region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.CharField(max_length=100, verbose_name='Nomi')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.Uzbekiston_provinces')),
            ],
            options={
                'verbose_name': '0002. Uzbekiston tumanlari',
                'verbose_name_plural': '0002. Uzbekiston tumanlari',
            },
        ),
    ]
