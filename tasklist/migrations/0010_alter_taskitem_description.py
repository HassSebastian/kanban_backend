# Generated by Django 4.2.5 on 2023-12-22 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasklist', '0009_delete_customuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskitem',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
