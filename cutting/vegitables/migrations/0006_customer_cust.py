# Generated by Django 5.0.7 on 2024-07-26 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vegitables', '0005_alter_customer_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='cust',
            field=models.CharField(default='default_value', max_length=100),
        ),
    ]
