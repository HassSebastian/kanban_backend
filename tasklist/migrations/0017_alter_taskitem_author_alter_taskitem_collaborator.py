# Generated by Django 4.2.5 on 2024-01-01 13:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tasklist', '0016_alter_taskitem_collaborator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskitem',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tasklist.member'),
        ),
        migrations.AlterField(
            model_name='taskitem',
            name='collaborator',
            field=models.ManyToManyField(blank=True, related_name='collaborated_tasks', to='tasklist.member'),
        ),
    ]
