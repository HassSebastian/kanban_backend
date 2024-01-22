from django.contrib import admin
from django.urls import path
from tasklist.fuctions import get_all_members
from tasklist.views import (
    LoginView,
    RegistView,
    TaskItemDetailView,
    TaskItemView,
)
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("regist/", RegistView.as_view(), name="regist"),
    path("board/", TaskItemView.as_view(), name="taskitem"),
    path("board/<int:pk>", TaskItemDetailView.as_view(), name="taskitemdetail"),
    path("board/api/get_all_members/", get_all_members, name="get_all_members"),
]

"""
URL Patterns for Task Management App.

Available Endpoints:
- 'admin/': Django admin interface.
- 'login/': POST - Log in and obtain authentication token.
- 'logout/': POST - Log out.
- 'register/': POST - Register a new user.
- 'board/': GET - List all tasks, POST - Create a new task.
- 'board/<int:pk>/': GET - Retrieve a specific task, PUT - Update a specific task, DELETE - Delete a specific task.
- 'board/api/get_all_members/': GET - Retrieve information about all members and return it in a JSON response.

Note: Ensure to include these URL patterns in your Django project's main `urls.py`.
"""
