# Generated by Django 4.1.7 on 2023-04-08 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0016_alter_projects_full description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projects',
            name='project',
        ),
    ]
