from django.contrib import admin
from django.urls import path

from tasklist.views import LoginView, TaskItemDetailView, TaskItemView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view()),
    path('board/', TaskItemView.as_view()),
    path('board/<int:pk>', TaskItemDetailView.as_view()),

]
