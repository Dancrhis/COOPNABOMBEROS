# Generated by Django 4.0.3 on 2022-07-11 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conabom', '0026_imagenesgaleria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beneficiario',
            name='cedula',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='beneficiario',
            name='telefono',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='socio',
            name='cedula',
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='socio',
            name='celular',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='socio',
            name='fechaSolicitud',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='socio',
            name='telefono',
            field=models.BigIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='socio',
            name='telefonoLugarTrabajo',
            field=models.BigIntegerField(),
        ),
    ]
