# Generated by Django 2.2.3 on 2021-04-30 06:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0008_auto_20210428_1218'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='citizenship',
            options={'verbose_name': '1. FUQAROLIK (BAZASI)', 'verbose_name_plural': '1. FUQAROLIK (BAZASI)'},
        ),
        migrations.AlterModelOptions(
            name='employment',
            options={'verbose_name': 'BANDLIK (BAZASI)', 'verbose_name_plural': 'BANDLIK (BAZASI)'},
        ),
        migrations.AlterModelOptions(
            name='professiona',
            options={'verbose_name': "01. PROFESSIONAL BO'LIM (Tajribali ishchilar)", 'verbose_name_plural': "01. PROFESSIONAL YO'NALISH (Tajribali ishchilar)"},
        ),
        migrations.AlterModelOptions(
            name='relocation',
            options={'verbose_name': "BOSHQA JOYGA KO'CHISH (BAZASI)", 'verbose_name_plural': "BOSHQA JOYGA KO'CHISH (BAZASI)"},
        ),
        migrations.AlterModelOptions(
            name='schedule',
            options={'verbose_name': 'ISH GRAFIGI (BAZASI)', 'verbose_name_plural': 'ISH GRAFIGI (BAZASI)'},
        ),
        migrations.AlterModelOptions(
            name='specialization',
            options={'verbose_name': "MUTAXASSISLIKLAR TAJRIBA YO'Q (BAZASI)", 'verbose_name_plural': "MUTAXASSISLIKLAR TAJRIBA YO'Q (BAZASI)"},
        ),
        migrations.AlterModelOptions(
            name='thchoprofar',
            options={'verbose_name': '02. MUTAXASISLIKLAR (Tajribali ishchilar)', 'verbose_name_plural': '02. MUTAXASISLIKLAR (Tajribali ishchilar)'},
        ),
        migrations.AlterModelOptions(
            name='uzbekiston_provinces',
            options={'verbose_name': "2. O'ZBEKISTON VILOYATLARI (BAZASI)", 'verbose_name_plural': "2. O'ZBEKISTON VILOYATLARI (BAZASI)"},
        ),
        migrations.AlterModelOptions(
            name='uzbekiston_region',
            options={'verbose_name': "3. O'ZBEKISTON TUMANLAR (BAZASI)", 'verbose_name_plural': "3. O'ZBEKISTON TUMANLAR (BAZASI)"},
        ),
    ]
