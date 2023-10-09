# myapp/tests.py
from django.test import TestCase
from apps.base_api.models import PersonModel
from django.test import Client
import pytest
from faker import Faker


fake = Faker()


class PersonModelTestCase(TestCase):
    def setUp(self):
        # Create a sample Product instance for testing
        self.person_1 = PersonModel.objects.create(
            name=fake.name(), email=fake.email(), phone=fake.phone_number()
        )
        self.person_2 = PersonModel.objects.create(
            name=fake.name(), email=fake.email(), phone=fake.phone_number()
        )

    @pytest.mark.django_db
    def test_get_person_by_id(self):
        # Create a sample product in the database
        person = PersonModel.objects.create(
            name="Person A", email="test@test.com", phone="123458694"
        )

        client = Client()

        response = client.get("/api/person/", args=[person.pk])

        # Check if the response status code is 200 (OK)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_post_with_failed_phone_number(self):
        client = Client()

        response = client.post(
            "/api/person/",
            {"name": "Test", "email": "email@email.com", "phone": "12312dk"},
        )

        # Check if the response status code is 400 (Error)
        assert response.status_code == 400

        # Check if the response contains the expected JSON data
        expected_data = {"phone": ["Only numeric characters are allowed."]}
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
