from django.db import models
from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    RegexValidator,
    MinLengthValidator,
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


class SellModel(models.Model):
    invoice = models.CharField(
        max_length=10,
        validators=[
            RegexValidator(
                regex=r"^[0-9]+$",
                message="Only numeric characters are allowed.",
                code="invalid_numeric_value",
            ),
            MinLengthValidator(
                limit_value=10, message="Invoice must have only 10 characters."
            ),
        ],
        unique=True,
    )

    sell_date = models.DateTimeField(null=True)

    client = models.ForeignKey(ClientModel, models.DO_NOTHING)

    seller = models.ForeignKey(SellerModel, models.DO_NOTHING)

    products = models.ManyToManyField(ProductModel, through="SellProductModel")


class SellProductModel(models.Model):
    product_id = models.ForeignKey(
        ProductModel,
        models.DO_NOTHING,
        db_column="product_id",
        related_name="product_sellproduct",
    )

    sell_id = models.ForeignKey(
        SellModel,
        models.DO_NOTHING,
        related_name="sell_sellproduct",
    )

    quantity = models.PositiveIntegerField(default=1)

    def subtotal(self):
        # Calculate the subtotal price for this product in the sell
        return self.product.unit_value * self.quantity

    class Meta:
        db_table = "sell_product"
        unique_together = (("product_id", "sell_id"),)
