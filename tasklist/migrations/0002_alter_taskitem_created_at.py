# Generated by Django 4.2.5 on 2023-10-26 11:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasklist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskitem',
            name='created_at',
            field=models.DateTimeField(default=datetime.date.today),
        ),
    ]
