# Generated by Django 2.1.7 on 2019-02-15 18:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('finanzas', '0007_corte'),
    ]

    operations = [
        migrations.AlterField(
            model_name='corte',
            name='fechacorte',
            field=models.DateField(default=django.utils.timezone.now, help_text='Fecha de registro', verbose_name='Fecha de registro'),
        ),
    ]