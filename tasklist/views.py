import json
from django import forms
from django.shortcuts import render, redirect
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from kanban_backend.serializers import RegistListSerializer, TaskItemSerialisierer
from tasklist.models import Regist, TaskItem
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from rest_framework import status, generics
from django.contrib.auth.forms import UserCreationForm


class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        return Response(
            {
                "token": token.key,
                "user_id": user.pk,
                "username": user.username,
                "password": user.password,
            }
        )


class RegistView(APIView):
    def post(self, request, format=None):
        serializer = RegistListSerializer(data=request.data)
        if serializer.is_valid():
            if Regist.objects.filter(email=request.data["email"]).exists():
                return Response(
                    {"error": "Diese E-Mail-Adresse existiert bereits"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskItemView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        tasks = TaskItem.objects.all()
        serializer = TaskItemSerialisierer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        task = request.data.copy()
        task["author"] = request.user.id
        serializer = TaskItemSerialisierer(data=task)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskItemDetailView(APIView):
    def get_object_or_404(self, pk):
        return TaskItem.objects.get(pk=pk)

    def delete(self, request, pk, format=None):
        task = self.get_object_or_404(pk)
        print(task)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        update_task = request.data.copy()
        task = self.get_object_or_404(pk)
        task.author = request.user.id
        serializer = TaskItemSerialisierer(task, data=update_task)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# def get_all_members(request):
#     members = User.objects.all()
#     print("members = ",members)
#     return JsonResponse(list(members), safe=False)


# def get_all_members(request):
#     members = User.objects.all()
#     serialized_members = [{'username': member.username, 'email': member.email} for member in members]
#     return JsonResponse(serialized_members, safe=False)


# def get_all_members(request):
#     all_members = Member.objects.all()
#     serializer = MembersSerialisierer(all_members)
#     # all_members ist jetzt ein Queryset mit allen Mitgliedern
#     # return render(request, 'members/all_members.html', {'members': all_members})
#     return JsonResponse(serializer.data)
