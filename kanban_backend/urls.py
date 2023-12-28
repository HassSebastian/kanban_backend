from django.contrib import admin
from django.urls import path

from tasklist.views import LoginView, TaskItemDetailView, TaskItemView, get_all_members

urlpatterns = [
    path("admin/", admin.site.urls),
    path("login/", LoginView.as_view()),
    path("board/", TaskItemView.as_view()),
    path("board/<int:pk>", TaskItemDetailView.as_view()),
    path('api/get_all_members/', get_all_members, name='get_all_members'),
]
