from apps.base_api.serializers import (
    ProductSerializer,
    PersonSerializer,
    SellerSerializer,
    ClientSerializer,
    ComissionSerializer,
    SellSerializer,
    SellProductSerializer,
)
from .models import (
    ProductModel,
    PersonModel,
    SellerModel,
    ClientModel,
    ComissionModel,
    SellModel,
    SellProductModel,
)
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError as DRFValidationError
from datetime import datetime, timedelta
from utils.helpers import check_day_week


class ProductViewSet(ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ["post", "get", "patch", "delete"]


class PersonViewSet(ModelViewSet):
    queryset = PersonModel.objects.all()
    serializer_class = PersonSerializer
    http_method_names = ["post", "get", "patch", "delete"]


class SellerViewSet(ModelViewSet):
    queryset = SellerModel.objects.all()
    serializer_class = SellerSerializer
    http_method_names = ["post", "get", "patch", "delete"]

    @action(detail=False, methods=["GET"], name="get_comission")
    def get_comission(self, request, *args, **kwargs):
        sellers = self.queryset
        start_date = datetime.strptime(
            request.query_params.get("start_date"), "%d/%m/%Y"
        )
        end_date = datetime.strptime(
            request.query_params.get("end_date"), "%d/%m/%Y"
        )

        data = []
        for seller in sellers:
            sells = SellModel.objects.filter(
                seller=seller,
                sell_date__range=(
                    start_date,
                    end_date + timedelta(days=1),
                ),
            ).all()
            if len(sells) > 0:
                total_comission = 0
                for sell in sells:
                    sell_product = sell.sell_sellproduct.first()
                    if sell_product is not None:
                        total_comission += sell_product.subtotal_comission()
                data.append(
                    {
                        "seller": PersonSerializer(seller.id_person).data,
                        "total_comission": "{:.2f}".format(total_comission),
                    }
                )
            else:
                data.append(
                    {
                        "seller": PersonSerializer(seller.id_person).data,
                        "total_comission": "Didn't sell anything on the date range specified.",
                    }
                )

        return Response({"status": 200, "data": data})


class ClientViewSet(ModelViewSet):
    queryset = ClientModel.objects.all()
    serializer_class = ClientSerializer
    http_method_names = ["post", "get", "patch", "delete"]


class ComissionViewSet(ModelViewSet):
    queryset = ComissionModel.objects.all()
    serializer_class = ComissionSerializer
    http_method_names = ["post", "get", "patch", "delete"]

    def update(self, request, *args, **kwargs):
        day_week = request.data.get("day_week")
        check_days = check_day_week(kwargs["pk"], day_week)

        if check_days["sucess"]:
            min = request.data.get("day_comission_perc_min")
            max = request.data.get("day_comission_perc_max")
            if min > max:
                return Response(
                    status=400,
                    data={
                        "sucess": False,
                        "message": "Minimun percentage cannot be higher than Maximum percentage.",
                    },
                )
            response = super().update(request, *args, **kwargs)
            return response
        else:
            return Response(status=400, data=check_days)


class SellViewSet(ModelViewSet):
    queryset = SellModel.objects.all()
    serializer_class = SellSerializer
    http_method_names = ["post", "get", "patch", "delete"]

    def create(self, request, *args, **kwargs):
        client_id = request.data.get("client")
        seller_id = request.data.get("seller")
        invoice = request.data.get("invoice")
        products_data = request.data.get("products", [])

        try:
            client = ClientModel.objects.get(id=client_id)
        except ClientModel.DoesNotExist:
            return Response(
                {"error": f"Client with ID {client_id} does not exist."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        try:
            seller = SellerModel.objects.get(id=seller_id)
        except SellerModel.DoesNotExist:
            return Response(
                {"error": f"Client with ID {seller_id} does not exist."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Create a Sell instance
        new_sell = SellModel.objects.create(
            sell_date=datetime.now(),
            client=client,
            seller=seller,
            invoice=invoice,
        )

        # Iterate over the products_data and create SellProduct instances
        for product_data in products_data:
            product_id = product_data.get("product_id")
            quantity = product_data.get("quantity")

            # Fetch the Product instance based on the product_id
            try:
                product = ProductModel.objects.get(id=product_id)
            except ProductModel.DoesNotExist:
                return Response(
                    {"error": f"Product with ID {product_id} does not exist."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            # Create the SellProduct instance and associate it with the Sell
            new_sell.sell_sellproduct.create(
                product_id=product, quantity=quantity
            )

        return Response(
            status=status.HTTP_201_CREATED, data=SellSerializer(new_sell).data
        )


class SellProductViewSet(ModelViewSet):
    queryset = SellProductModel.objects.all()
    serializer_class = SellProductSerializer
    http_method_names = ["get", "patch"]
