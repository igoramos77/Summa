# Generated by Django 3.1.7 on 2021-06-06 07:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('summa', '0016_delete_categoriacursoatividadecomplementar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoriacurso',
            name='curso',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='summa.curso'),
        ),
    ]