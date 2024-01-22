from django.test import TestCase
from django.urls import reverse

class UrlsTest(TestCase):
    def test_login_url(self):
        # Überprüfen Sie, ob die Login-URL korrekt konfiguriert ist
        login_url = reverse("login")
        self.assertEqual(login_url, "/login/")  # Passen Sie dies entsprechend Ihrer Konfiguration an

    def test_logout_url(self):
        # Überprüfen Sie, ob die Logout-URL korrekt konfiguriert ist
        logout_url = reverse("logout")
        self.assertEqual(logout_url, "/logout/")  # Passen Sie dies entsprechend Ihrer Konfiguration an

    def test_regist_url(self):
        # Überprüfen Sie, ob die Registrierungs-URL korrekt konfiguriert ist
        regist_url = reverse("regist")
        self.assertEqual(regist_url, "/regist/")  # Passen Sie dies entsprechend Ihrer Konfiguration an

    def test_task_item_url(self):
        # Überprüfen Sie, ob die URL für TaskItem korrekt konfiguriert ist
        task_item_url = reverse("taskitem")
        self.assertEqual(task_item_url, "/board/")  # Passen Sie dies entsprechend Ihrer Konfiguration an

    def test_task_item_detail_url(self):
        # Überprüfen Sie, ob die URL für TaskItemDetailView korrekt konfiguriert ist
        task_item_detail_url = reverse("taskitemdetail", args=[1])  # Beispiel für eine PK
        self.assertEqual(task_item_detail_url, "/board/1")  # Passen Sie dies entsprechend Ihrer Konfiguration an

    def test_get_all_members_url(self):
        # Überprüfen Sie, ob die URL für get_all_members korrekt konfiguriert ist
        get_all_members_url = reverse("get_all_members")
        self.assertEqual(get_all_members_url, "/board/api/get_all_members/")  # Passen Sie dies entsprechend Ihrer Konfiguration an
