# Generated by Django 4.2.5 on 2023-10-26 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasklist', '0003_alter_taskitem_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskitem',
            name='colorItem',
            field=models.SmallIntegerField(choices=[(0, 'Yellow'), (1, 'Blue'), (2, 'Green'), (3, 'Orange'), (4, 'Red'), (5, 'Cyan'), (6, 'Purple'), (7, 'Magenta')], default=0),
        ),
    ]
