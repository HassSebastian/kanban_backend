from audioop import reverse
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from tasklist.models import TaskItem



class TaskItemViewTest(TestCase):
    def setUp(self):
        # Set up a test user with a token
        self.user = User.objects.create_user(username="testuser", password="testpassword")
        self.token = Token.objects.create(user=self.user)

        # Set up some test data
        self.task1 = TaskItem.objects.create(title="Task 1", description="Description 1", author=self.user)
        self.task2 = TaskItem.objects.create(title="Task 2", description="Description 2", author=self.user)

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')
        self.board_url = reverse("taskitem")

    def test_get_task_list(self):
        """
        Test retrieving a list of TaskItems using HTTP GET.
        """
        response = self.client.get(self.board_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Assuming two tasks in the test data
        self.assertContains(response, "Task 1")
        self.assertContains(response, "Task 2")

    def test_unauthenticated_access(self):
        """
        Test that unauthenticated users cannot access the TaskItemView.
        """
        # Clear credentials to simulate an unauthenticated request
        self.client.credentials()

        response = self.client.get(self.board_url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # Add more test cases as needed
