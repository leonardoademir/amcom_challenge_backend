# Generated by Django 4.2.5 on 2023-10-08 15:04

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base_api", "0002_comissionmodel"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comissionmodel",
            name="day_comission_perc_max",
            field=models.FloatField(
                null=True,
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
        migrations.AlterField(
            model_name="comissionmodel",
            name="day_comission_perc_min",
            field=models.FloatField(
                null=True,
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
