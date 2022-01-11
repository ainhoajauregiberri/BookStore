# Generated by Django 3.2.9 on 2021-11-20 15:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('biografia', models.CharField(max_length=800)),
                ('imagenLink', models.CharField(max_length=800)),
            ],
        ),
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('explicacion', models.CharField(max_length=800)),
                ('imagenLink', models.CharField(max_length=800)),
            ],
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Idioma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('paginas', models.IntegerField(default=0)),
                ('sinopsis', models.CharField(max_length=800)),
                ('fechaPubli', models.DateField()),
                ('imagenLink', models.CharField(max_length=800)),
                ('autores', models.ManyToManyField(to='appBookStore.Autor')),
                ('editorial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appBookStore.editorial')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appBookStore.genero')),
                ('idioma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appBookStore.idioma')),
            ],
        ),
    ]