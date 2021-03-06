# Generated by Django 2.2.3 on 2021-04-28 09:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0008_auto_20210428_1218'),
        ('summary', '0013_auto_20210428_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='summary',
            name='profess',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.Professiona'),
        ),
        migrations.AddField(
            model_name='summary',
            name='speciali',
            field=models.ManyToManyField(to='category.Specialization'),
        ),
        migrations.AddField(
            model_name='summary',
            name='thchopr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='category.Thchoprofar'),
        ),
    ]
