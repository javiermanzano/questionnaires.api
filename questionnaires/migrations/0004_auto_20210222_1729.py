# Generated by Django 3.1.7 on 2021-02-22 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaires', '0003_delete_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collecteddata',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]