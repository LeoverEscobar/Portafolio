# Generated by Django 4.2.7 on 2023-11-04 00:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ubicaciones', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lugares',
            options={'ordering': ['name'], 'verbose_name': 'Sucursal', 'verbose_name_plural': 'Sucursales'},
        ),
        migrations.RenameField(
            model_name='lugares',
            old_name='Name',
            new_name='name',
        ),
    ]