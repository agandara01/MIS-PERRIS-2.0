# Generated by Django 2.1.2 on 2018-11-12 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0003_persona_foto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameD', models.CharField(max_length=40)),
                ('cantidad', models.CharField(max_length=40)),
                ('desc', models.CharField(max_length=40)),
                ('fotoD', models.ImageField(upload_to='fotos/')),
            ],
        ),
    ]