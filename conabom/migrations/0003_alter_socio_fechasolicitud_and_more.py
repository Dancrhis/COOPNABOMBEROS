# Generated by Django 4.0.3 on 2022-05-09 03:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conabom', '0002_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socio',
            name='fechaSolicitud',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 8, 23, 47, 25, 3330)),
        ),
        migrations.AlterField(
            model_name='socio',
            name='fechaValidacion',
            field=models.DateTimeField(null=True),
        ),
    ]
