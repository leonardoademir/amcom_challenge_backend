from django.db import models
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    RegexValidator,
)


class ProductModel(models.Model):
    code = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    unit_value = models.FloatField()
    comis_percentage = models.FloatField(
        validators=[
            MinValueValidator(
                limit_value=0.0,
                message="Value must be greater than or equal to 0.0",
            ),
            MaxValueValidator(
                limit_value=100.0,
                message="Value must be less than or equal to 100.0",
            ),
        ]
    )


class PersonModel(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(null=True)
    phone = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r"^[0-9]+$",
                message="Only numeric characters are allowed.",
                code="invalid_numeric_value",
            ),
        ],
    )


class SellerModel(models.Model):
    id_person = models.ForeignKey(
        PersonModel, models.DO_NOTHING, related_name="person_seller"
    )

    # Any other needed attribute for specific seller model


class ClientModel(models.Model):
    id_person = models.ForeignKey(
        PersonModel, models.DO_NOTHING, related_name="person_client"
    )

    # Any other needed attribute for specific client model


class ComissionModel(models.Model):
    day_week = models.CharField(max_length=3)
    day_comission_perc_min = models.FloatField(
        validators=[
            MinValueValidator(
                limit_value=0.0,
                message="Value must be greater than or equal to 0.0",
            ),
            MaxValueValidator(
                limit_value=100.0,
                message="Value must be less than or equal to 100.0",
            ),
        ],
        null=True,
    )
    day_comission_perc_max = models.FloatField(
        validators=[
            MinValueValidator(
                limit_value=0.0,
                message="Value must be greater than or equal to 0.0",
            ),
            MaxValueValidator(
                limit_value=100.0,
                message="Value must be less than or equal to 100.0",
            ),
        ],
        null=True,
    )
