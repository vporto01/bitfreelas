# Generated by Django 4.1.7 on 2023-04-04 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_alter_project_currency'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='freelancer',
        ),
    ]
