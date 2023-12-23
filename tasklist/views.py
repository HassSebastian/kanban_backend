import json
from django import forms
from django.shortcuts import render, redirect
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from kanban_backend.serializers import TaskItemSerialisierer
from tasklist.models import TaskItem
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from rest_framework import status




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
        
        
class TaskItemView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        tasks = TaskItem.objects.all()
        serializer = TaskItemSerialisierer(tasks, many=True)
        return Response(serializer.data)



class TaskItemDetailView(APIView):
    def get_object_or_404(self, pk):
        return TaskItem.objects.get(pk=pk)
    

    def delete(self, request, pk, format=None):
        task = self.get_object_or_404(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
