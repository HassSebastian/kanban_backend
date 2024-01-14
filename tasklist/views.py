# from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from kanban_backend.serializers import TaskItemSerialisierer
from tasklist.models import TaskItem
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.decorators import api_view


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
                # "username": user.username,
                # "password": user.password,
            }
        )


class RegistView(APIView):
    def post(self, request, format=None):
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        email = request.data.get("email")
        username = request.data.get("username")
        if User.objects.filter(email=email).exists():
            return Response(
                {"error": "This username is already taken"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
        )
        user.set_password(request.data.get("password"))
        user.save()
        return Response(
            {"message": "User registered successfully"}, status=status.HTTP_201_CREATED
        )


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


def get_all_members(request):
    members = User.objects.all()
    serialized_members = [
        {
            "user_id": member.id,
            "username": member.username,
            "email": member.email,
            "first_name": member.first_name,
            "last_name": member.last_name,
            "checked": False,
            "color": get_member_color(member),
            "initials": get_member_initials(member),
        }
        for member in members
    ]
    return JsonResponse(serialized_members, safe=False)


def get_member_color(member):
    if exist_first_and_last_name(member):
        ascii_first_letter = ord(member.first_name[0])
        ascii_second_letter = ord(member.last_name[0])
        sum = ascii_first_letter + ascii_second_letter
        color_index = sum % 7
        return color_index
    elif exist_username(member):
        ascii_username_first_letter = ord(member.username[0])
        ascii_username_second_letter = ord(member.username[1])
        sum = ascii_username_first_letter + ascii_username_second_letter
        color_index = sum % 7
        return color_index
    else:
        return ""


def get_member_initials(member):
    if exist_first_and_last_name(member):
        return member.first_name[0] + member.last_name[0].upper()
    elif exist_username(member):
        return member.username[:2].upper()
    else:
        return ""


def exist_first_and_last_name(member):
    return bool(member.first_name and member.last_name)


def exist_username(member):
    return bool(member.username)


# def get_all_members(request):
#     all_members = Member.objects.all()
#     serializer = MembersSerialisierer(all_members)
#     # all_members ist jetzt ein Queryset mit allen Mitgliedern
#     # return render(request, 'members/all_members.html', {'members': all_members})
#     return JsonResponse(serializer.data)

