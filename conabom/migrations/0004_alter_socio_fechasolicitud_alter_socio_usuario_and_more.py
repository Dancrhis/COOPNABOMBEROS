# Generated by Django 4.0.3 on 2022-05-11 01:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conabom', '0003_alter_socio_fechasolicitud_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socio',
            name='fechaSolicitud',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 10, 21, 18, 18, 197994)),
        ),
        migrations.AlterField(
            model_name='socio',
            name='usuario',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
