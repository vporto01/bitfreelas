# Generated by Django 4.1.7 on 2023-04-09 18:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_freelancer_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]