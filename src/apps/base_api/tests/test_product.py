# myapp/tests.py
from django.test import TestCase
from apps.base_api.models import ProductModel
from django.test import Client

import pytest


class ProductModelTestCase(TestCase):
    def setUp(self):
        # Create a sample Product instance for testing
        self.product_1 = ProductModel.objects.create(
            code="1234",
            description="Test",
            unit_value=4.0,
            comis_percentage=2.0,
        )
        self.product_2 = ProductModel.objects.create(
            code="983120",
            description="Test1234",
            unit_value=98.0,
            comis_percentage=23.0,
        )

    def test_product_creation(self):
        """
        Test whether a Product instance is created correctly.
        """
        self.assertEqual(self.product_1.code, "1234")
        self.assertEqual(self.product_1.description, "Test")
        self.assertEqual(self.product_1.unit_value, 4.0)
        self.assertEqual(self.product_1.comis_percentage, 2.0)

    def test_product_description(self):
        # Retrieve a product from the database
        product_b = ProductModel.objects.get(description="Test1234")

        # Check if the product's name is as expected
        self.assertEqual(product_b.description, "Test1234")

    @pytest.mark.django_db
    def test_post_with_failed_comis_percentage(self):
        client = Client()

        response = client.post(
            "/api/product/",
            {
                "code": "12344",
                "description": "test_POST",
                "unit_value": 123.0,
                "comis_percentage": 140.0,
            },
        )

        # Check if the response status code is 400 (Error)
        assert response.status_code == 400

        # Check if the response contains the expected JSON data
        expected_data = {
            "comis_percentage": [
                "Ensure this value is less than or equal to 100.0."
            ]
        }
        assert response.json() == expected_data

    @pytest.mark.django_db
    def test_post_product_sucessfull(self):
        client = Client()

        response = client.post(
            "/api/product/",
            {
                "code": "12344",
                "description": "test_POST",
                "unit_value": 123.0,
                "comis_percentage": 98.0,
            },
        )

        # Check if the response status code is 201 (created)
        assert response.status_code == 201
