# Generated by Django 5.0.1 on 2024-09-29 15:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_remove_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='shop',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='app.shopreg'),
            preserve_default=False,
        ),
    ]
