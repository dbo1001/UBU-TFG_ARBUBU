# Generated by Django 2.2 on 2019-05-09 18:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pantallaPrincipal', '0012_auto_20190509_2027'),
    ]

    operations = [
        migrations.RenameField(
            model_name='individuos',
            old_name='especie',
            new_name='tipoEspecie',
        ),
    ]
