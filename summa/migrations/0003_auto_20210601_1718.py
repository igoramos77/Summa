# Generated by Django 3.1.7 on 2021-06-01 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('summa', '0002_atividadecomplementar_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividadecomplementar',
            name='carga_horaria_integralizada',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Carga Horária Integralizada'),
        ),
    ]