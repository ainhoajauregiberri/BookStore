# Generated by Django 2.2.3 on 2021-11-13 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appBookStore', '0008_auto_20211113_2233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='libro',
            name='fecha_publi',
        ),
    ]