# Generated by Django 2.2 on 2019-05-27 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pantallaPrincipal', '0041_auto_20190527_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individuos',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
