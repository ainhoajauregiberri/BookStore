# Generated by Django 3.2.9 on 2021-11-16 13:23

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('appBookStore', '0015_auto_20211114_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='fechaPubli',
            field=models.DateField(default=datetime.datetime(2021, 11, 16, 13, 23, 55, 492824, tzinfo=utc)),
        ),
    ]