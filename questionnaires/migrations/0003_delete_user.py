# Generated by Django 3.1.7 on 2021-02-21 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaires', '0002_auto_20210221_2014'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]