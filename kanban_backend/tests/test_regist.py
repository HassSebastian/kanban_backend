from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth.models import User
from django.urls import reverse


class UserRegistrationTest(TestCase):
    def setUp(self):
        # Richten Sie einen Testbenutzer für vorhandene Daten ein
        self.existing_user = User.objects.create_user(
            username="existing_user",
            email="existing@example.com",
            password="existing_password",
        )

        self.client = APIClient()
        self.regist_url = reverse("regist")

    def test_successful_registration(self):
        """
        Test a successful user registration.
        """
        data = {
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "username": "johndoe",
            "password": "password123",
        }

        response = self.client.post(self.regist_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
            User.objects.count(), 2
        )  # Es werden nur der bestehende Benutzer und der neue Benutzer angenommen
        self.assertTrue(User.objects.filter(username="johndoe").exists())

    def test_duplicate_email_registration(self):
        """
        Die Testregistrierung mit einer doppelten E-Mail-Adresse sollte fehlschlagen.
        """
        data = {
            "first_name": "Jane",
            "last_name": "Doe",
            "email": self.existing_user.email,  # Verwendung einer vorhandenen E-Mail
            "username": "janedoe",
            "password": "password456",
        }

        response = self.client.post(self.regist_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            User.objects.count(), 1
        )  # Es sollte kein neuer Benutzer erstellt werden
