# Generated by Django 3.2.9 on 2021-12-23 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appBookStore', '0005_usuario_notificar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='notificar',
            field=models.BooleanField(default=False),
        ),
    ]