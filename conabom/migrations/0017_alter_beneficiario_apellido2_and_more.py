# Generated by Django 4.0.3 on 2022-06-19 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conabom', '0016_alter_socio_fechasolicitud'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficiario',
            name='apellido2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='beneficiario',
            name='nombre2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
