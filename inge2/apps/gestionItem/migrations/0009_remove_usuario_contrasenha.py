# Generated by Django 2.2.6 on 2019-11-15 14:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionItem', '0008_auto_20191108_1352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='contrasenha',
        ),
    ]