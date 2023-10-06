from rest_framework import serializers
from .models import (
    ProductModel,
    PersonModel,
    SellerModel,
    ClientModel,
)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = "__all__"


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonModel
        fields = "__all__"


class SellerSerializer(serializers.ModelSerializer):
    person = PersonSerializer()

    class Meta:
        model = SellerModel
        fields = "__all__"


class ClientSerializer(serializers.ModelSerializer):
    person = PersonSerializer()

    class Meta:
        model = ClientModel
        fields = "__all__"
