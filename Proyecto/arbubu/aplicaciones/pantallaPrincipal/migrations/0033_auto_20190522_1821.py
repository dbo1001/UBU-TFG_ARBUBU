# Generated by Django 2.2 on 2019-05-22 16:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pantallaPrincipal', '0032_auto_20190522_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='individuos',
            name='nombreComun',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='pantallaPrincipal.Especie'),
        ),
    ]
