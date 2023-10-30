# Generated by Django 4.2.5 on 2023-10-26 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasklist', '0006_rename_coloritem_taskitem_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskitem',
            name='color',
            field=models.SmallIntegerField(choices=[(0, 'Yellow'), (1, 'Blue'), (2, 'Green'), (3, 'Orange'), (4, 'Red'), (5, 'Cyan'), (6, 'Purple')], default=0),
        ),
    ]
