# Generated by Django 3.2.9 on 2021-11-14 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appBookStore', '0014_auto_20211113_2251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='fecha_publi',
        ),
        migrations.AlterField(
            model_name='autor',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='editorial',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='genero',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='idioma',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='libro',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]