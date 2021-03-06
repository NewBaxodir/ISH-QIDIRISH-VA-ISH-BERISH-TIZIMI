# Generated by Django 2.2.3 on 2021-04-28 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('summary', '0009_summary_workexper'),
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
        migrations.AlterField(
            model_name='workexperience',
            name='organiza',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='position',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='workexperience', to='summary.Summary'),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='workplaceres',
            field=models.TextField(blank=True, verbose_name='Ish joyingizdagi vazifa haqida yozing'),
        ),
    ]
