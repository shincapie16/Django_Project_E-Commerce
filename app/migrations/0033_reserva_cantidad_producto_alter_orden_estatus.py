# Generated by Django 4.1.1 on 2022-11-21 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0032_reserva'),
    ]

    operations = [
        migrations.AddField(
            model_name='reserva',
            name='cantidad_producto',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='orden',
            name='estatus',
            field=models.CharField(choices=[('Completado', 'Completado'), ('Pendiente', 'Pendiente'), ('En envio', 'En envio')], default='Pendiente', max_length=150),
        ),
    ]
