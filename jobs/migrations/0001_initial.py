# Generated by Django 4.2.1 on 2023-05-28 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('contenido', models.CharField(max_length=100)),
                ('autor', models.CharField(max_length=50)),
                ('ubicacion', models.CharField(max_length=20)),
                ('imagen', models.ImageField(upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'empleo',
                'verbose_name_plural': 'empleos',
            },
        ),
    ]
