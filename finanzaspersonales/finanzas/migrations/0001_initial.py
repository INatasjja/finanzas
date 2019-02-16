# Generated by Django 2.1.7 on 2019-02-15 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TipoEgresos',
            fields=[
                ('id', models.AutoField(help_text='ID único', primary_key=True, serialize=False)),
                ('descripcion', models.CharField(help_text='Descripcion del tipo de Egreso', max_length=200)),
                ('estado', models.CharField(blank=True, choices=[('A', 'Activo'), ('I', 'Inactivo')], default='A', help_text='Estado del egreso', max_length=1)),
            ],
        ),
    ]
