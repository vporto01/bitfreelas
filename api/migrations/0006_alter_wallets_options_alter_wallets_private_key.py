# Generated by Django 4.1.7 on 2023-04-10 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_wallets'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wallets',
            options={'verbose_name': 'Wallet', 'verbose_name_plural': 'Wallets'},
        ),
        migrations.AlterField(
            model_name='wallets',
            name='private_key',
            field=models.CharField(max_length=2000),
        ),
    ]