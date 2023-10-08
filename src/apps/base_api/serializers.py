from rest_framework import serializers
from .models import (
    ProductModel,
    PersonModel,
    SellerModel,
    ClientModel,
    ComissionModel,
    SellModel,
    SellProductModel,
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
    class Meta:
        model = SellerModel
        fields = "__all__"

    def to_representation(self, instance):
        self.fields["id_person"] = PersonSerializer(read_only=True)

        return super(SellerSerializer, self).to_representation(instance)


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientModel
        fields = "__all__"

    def to_representation(self, instance):
        self.fields["id_person"] = PersonSerializer(read_only=True)

        return super(ClientSerializer, self).to_representation(instance)


class ComissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ComissionModel
        fields = "__all__"


class SellSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = SellModel
        fields = "__all__"


class SellProductSerializer(serializers.ModelSerializer):
    product_id = ProductSerializer()
    client = serializers.SerializerMethodField()
    seller = serializers.SerializerMethodField()
    invoice = serializers.SerializerMethodField()
    sell_date = serializers.SerializerMethodField()

    class Meta:
        model = SellProductModel
        fields = "__all__"

    def to_representation(self, instance):
        return super(SellProductSerializer, self).to_representation(instance)

    def get_client(self, obj) -> dict:
        return ClientSerializer(obj.sell_id.client).data

    def get_seller(self, obj) -> dict:
        return SellerSerializer(obj.sell_id.seller).data

    def get_invoice(self, obj) -> str:
        return obj.sell_id.invoice

    def get_sell_date(self, obj) -> str:
        return obj.sell_id.sell_date
