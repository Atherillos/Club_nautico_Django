# Generated by Django 3.1.5 on 2021-03-16 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Socios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombre', models.CharField(max_length=60)),
                ('apellido', models.CharField(max_length=60)),
                ('dni', models.CharField(max_length=8)),
                ('telefono', models.CharField(max_length=15)),
                ('direccion', models.CharField(max_length=40)),
            ],
        ),
    ]
