# Generated by Django 5.0.6 on 2024-07-02 15:00

import account.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='pin',
            field=models.CharField(default='0000', max_length=4, validators=[account.validators.validate_pin]),
        ),
    ]
