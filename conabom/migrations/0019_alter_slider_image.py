# Generated by Django 4.0.3 on 2022-06-24 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conabom', '0018_alter_socio_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slider',
            name='image',
            field=models.ImageField(upload_to='conabom/pages/static/IMG/images/%y/%m/%d'),
        ),
    ]