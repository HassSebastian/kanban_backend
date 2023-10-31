# Generated by Django 4.2.5 on 2023-10-30 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasklist', '0007_alter_taskitem_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
    ]
