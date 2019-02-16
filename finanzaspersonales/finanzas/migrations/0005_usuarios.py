# Generated by Django 2.1.7 on 2019-02-15 18:25

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finanzas', '0004_auto_20190215_1405'),
    ]

    operations = [
        migrations.CreateModel(
            name='usuarios',
            fields=[
                ('id', models.AutoField(help_text='ID Usuario', primary_key=True, serialize=False)),
                ('primernombre', models.CharField(help_text='Primer Nombre', max_length=15, verbose_name='Primer Nombre')),
                ('segundonombre', models.CharField(help_text='Segundo Nombre', max_length=15, verbose_name='Segundo Nombre')),
                ('primerapellido', models.CharField(help_text='Primer Apellido', max_length=15, verbose_name='Primer Apellido')),
                ('segundoapellido', models.CharField(help_text='Segundo Apellido', max_length=15, verbose_name='Segundo Apellido')),
                ('cedula', models.CharField(help_text='Cedula', max_length=11, verbose_name='Cedula')),
                ('limiteegresos', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('tipopersona', models.CharField(blank=True, choices=[('F', 'Fisica'), ('J', 'Juridico')], default='A', help_text='Estado del tipo de pago', max_length=1, verbose_name='Estado')),
                ('fechacorte', models.DateField(help_text='Fecha de Corte', verbose_name='Fecha de Corte')),
                ('estado', models.CharField(blank=True, choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', help_text='Estado del tipo de pago', max_length=1, verbose_name='Estado')),
            ],
        ),
    ]
