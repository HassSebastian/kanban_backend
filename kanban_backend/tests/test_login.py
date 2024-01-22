from django.test import Client, TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework.authtoken.models import Token

        
class LoginViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        # self.client = APIClient()
        self.login_url = reverse("login")  # Stellen Sie sicher, dass Sie die richtige URL für Ihre Ansicht verwenden

        # Erstellen Sie einen Testbenutzer
        self.username = "testuser"
        self.password = "testpassword"
        self.user = User.objects.create_user(username=self.username, password=self.password)

    def test_login_view(self):
        # Rufen Sie die Login-Ansicht auf
        data = {"username": self.username, "password": self.password}
        response = self.client.post(self.login_url, data, format="json")

        # Überprüfen Sie, ob die Antwort erfolgreich ist (Statuscode 200)
        self.assertEqual(response.status_code, 200)

        # Überprüfen Sie, ob das Token in der Antwort enthalten ist
        self.assertIn("token", response.data)

        # Überprüfen Sie, ob der Benutzer-ID in der Antwort enthalten ist
        self.assertIn("user_id", response.data)

        # Überprüfen Sie, ob das Token für den richtigen Benutzer erstellt wurde
        token = Token.objects.get(user=self.user)
        self.assertEqual(response.data["token"], token.key)