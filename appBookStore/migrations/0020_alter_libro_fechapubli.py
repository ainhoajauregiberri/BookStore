# Generated by Django 3.2.9 on 2021-11-16 13:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('appBookStore', '0019_alter_libro_fechapubli'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='fechaPubli',
            field=models.DateField(default=datetime.datetime(2021, 11, 16, 13, 43, 35, 736922, tzinfo=utc)),
        ),
    ]
