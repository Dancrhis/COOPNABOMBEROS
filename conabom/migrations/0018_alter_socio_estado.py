# Generated by Django 4.0.3 on 2022-06-20 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conabom', '0017_alter_beneficiario_apellido2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socio',
            name='estado',
            field=models.CharField(default='en proceso', max_length=50),
        ),
    ]
