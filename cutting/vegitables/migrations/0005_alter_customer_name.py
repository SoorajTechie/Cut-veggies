# Generated by Django 5.0.7 on 2024-07-26 15:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vegitables', '0004_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vegitables.vegitables'),
        ),
    ]
