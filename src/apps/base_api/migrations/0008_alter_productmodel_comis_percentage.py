# Generated by Django 4.2.5 on 2023-10-08 22:49

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base_api", "0007_alter_productmodel_comis_percentage_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productmodel",
            name="comis_percentage",
            field=models.DecimalField(
                decimal_places=2,
                max_digits=5,
                validators=[
                    django.core.validators.MinValueValidator(
                        limit_value=0.0,
                        message="Value must be greater than or equal to 0.0",
                    ),
                    django.core.validators.MaxValueValidator(
                        limit_value=100.0,
                        message="Value must be less than or equal to 100.0",
                    ),
                ],
            ),
        ),
    ]