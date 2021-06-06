# Generated by Django 3.1.7 on 2021-06-06 06:47

from django.db import migrations
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('summa', '0009_auto_20210606_0315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='categoriacurso',
            name='categoria_atividade_complementar',
        ),
        migrations.AlterField(
            model_name='atividadecomplementar',
            name='categoria',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='curso', chained_model_field='categoriacurso_categoria_atividade_complementar', on_delete=django.db.models.deletion.CASCADE, sort=False, to='summa.categoriacurso'),
        ),
    ]
