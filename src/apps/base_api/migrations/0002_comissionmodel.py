# Generated by Django 4.2.5 on 2023-10-08 14:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base_api", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ComissionModel",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("day_week", models.CharField(max_length=3)),
                (
                    "day_comission_perc_min",
                    models.FloatField(
                        validators=[
                            django.core.validators.MinValueValidator(
                                limit_value=0.0,
                                message="Value must be greater than or equal to 0.0",
                            ),
                            django.core.validators.MaxValueValidator(
                                limit_value=100.0,
                                message="Value must be less than or equal to 100.0",
                            ),
                        ]
                    ),
                ),
                (
                    "day_comission_perc_max",
                    models.FloatField(
                        validators=[
                            django.core.validators.MinValueValidator(
                                limit_value=0.0,
                                message="Value must be greater than or equal to 0.0",
                            ),
                            django.core.validators.MaxValueValidator(
                                limit_value=100.0,
                                message="Value must be less than or equal to 100.0",
                            ),
                        ]
                    ),
                ),
            ],
        ),
    ]
