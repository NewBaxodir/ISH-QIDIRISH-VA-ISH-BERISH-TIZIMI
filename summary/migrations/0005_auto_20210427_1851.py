# Generated by Django 2.2.3 on 2021-04-27 15:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('summary', '0004_workexperience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workexperience',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workexperience', to='summary.Summary'),
        ),
        migrations.AlterModelTable(
            name='workexperience',
            table='workexperience',
        ),
    ]
