# Generated by Django 4.1.7 on 2023-04-05 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'usera', 'verbose_name_plural': 'users'},
        ),
    ]
