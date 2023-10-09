# Generated by Django 4.2.5 on 2023-10-08 22:42

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("base_api", "0006_alter_sellproductmodel_product_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productmodel",
            name="comis_percentage",
            field=models.DecimalField(
                decimal_places=2,
                max_digits=3,
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
            model_name="sellmodel",
            name="sell_date",
            field=models.DateTimeField(default=django.utils.timezone.now, null=True),
        ),
    ]