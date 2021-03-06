# Generated by Django 4.0.3 on 2022-06-25 23:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('conabom', '0019_alter_slider_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socio',
            name='acta',
            field=models.CharField(default='ninguna', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='socio',
            name='estado',
            field=models.CharField(choices=[('en proceso', 'en proceso'), ('aprobada', 'aprobada'), ('rechazada', 'recchazada')], default='en proceso', max_length=50),
        ),
        migrations.AlterField(
            model_name='socio',
            name='fechaValidacion',
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]
