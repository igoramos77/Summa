# Generated by Django 3.1.7 on 2021-06-02 14:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('summa', '0008_auto_20210602_1140'),
    ]

    operations = [
        migrations.RenameField(
            model_name='atividadecomplementar',
            old_name='certificado_img',
            new_name='certificado',
        ),
    ]