# Generated by Django 2.2.3 on 2021-11-13 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appBookStore', '0004_auto_20211113_2225'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='fechaPubli',
            field=models.DateField(),
        ),
    ]
