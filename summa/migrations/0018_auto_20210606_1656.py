# Generated by Django 3.1.7 on 2021-06-06 19:56

from django.db import migrations, models
import django.db.models.deletion
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('summa', '0017_auto_20210606_0454'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='categoria_atividade_complementar',
            field=models.ManyToManyField(to='summa.CategoriaAtividadeComplementar'),
        ),
        migrations.AlterField(
            model_name='atividadecomplementar',
            name='categoria',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='curso', chained_model_field='categoriacurso__categoriacurso_id', on_delete=django.db.models.deletion.CASCADE, sort=False, to='summa.categoriaatividadecomplementar'),
        ),
        migrations.DeleteModel(
            name='CategoriaCurso',
        ),
    ]
