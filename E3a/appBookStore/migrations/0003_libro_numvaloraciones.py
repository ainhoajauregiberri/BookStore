# Generated by Django 3.2.9 on 2021-12-19 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appBookStore', '0002_auto_20211219_1134'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='numValoraciones',
            field=models.IntegerField(default=0),
        ),
    ]
