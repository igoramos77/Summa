# Generated by Django 3.1.7 on 2021-06-03 19:07

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('summa', '0016_auto_20210603_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='external_id',
            field=models.UUIDField(default=uuid.uuid4, verbose_name='Hash Usuário'),
        ),
    ]