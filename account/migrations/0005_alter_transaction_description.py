# Generated by Django 5.0.6 on 2024-07-05 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_transaction_amount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='description',
            field=models.TextField(blank=True, default='description not provided', max_length=225),
        ),
    ]
