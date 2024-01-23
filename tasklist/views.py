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
    """
    A class-based view for handling user login and obtaining authentication tokens.

    Methods:
    - `post(self, request, *args, **kwargs)`: Handles HTTP POST request for user login.

    Attributes:
    - None
    """

    def post(self, request, *args, **kwargs):
        """
        Handles HTTP POST request for user login and obtaining authentication tokens.

        Args:
            request (HttpRequest): The HTTP request object.
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.

        Returns:
            Response: A Response object with authentication token and user information.
        """
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
            }
        )


class RegistView(APIView):
    """
    A class-based view for handling user registration.

    Methods:
    - `post(self, request, format=None)`: Handles HTTP POST request for user registration.

    Attributes:
    - None
    """

    def post(self, request, format=None):
        """
        Handles the HTTP POST request for user registration.

        Parameters:
        - request (rest_framework.request.Request): The HTTP request object.
        - format (str, optional): The requested format for the response. Defaults to None.

        Returns:
        - rest_framework.response.Response: HTTP response indicating the result of user registration.
        """
        data = request.data
        username = data.get("username")
        email = data.get("email")

        if User.objects.filter(username=username).exists():
            return Response(
                {"error": "This username is already taken"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if User.objects.filter(email=email).exists():
            return Response(
                {"error": "This email is already taken"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = User.objects.create_user(**data)
        return Response(
            {"message": "User registered successfully"}, status=status.HTTP_201_CREATED
        )


class TaskItemView(APIView):
    """
    A class-based view for handling operations on a collection of TaskItems.

    Attributes:
    - `authentication_classes` (list): List of authentication classes applied to the view.
    - `permission_classes` (list): List of permission classes applied to the view.
    """

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """
        Handles HTTP GET request to retrieve a list of TaskItems.

        Args:
            request (HttpRequest): The HTTP request object.
            format (str, optional): The requested format for the response. Defaults to None.

        Returns:
            Response: A Response object with serialized TaskItem data.
        """
        tasks = TaskItem.objects.all()
        serializer = TaskItemSerialisierer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        """
        Handles HTTP POST request to create a new TaskItem.

        Args:
            request (HttpRequest): The HTTP request object.
            format (str, optional): The requested format for the response. Defaults to None.

        Returns:
            Response: A Response object with the created TaskItem data or error messages.
        """
        task = request.data.copy()
        task["author"] = request.user.id
        serializer = TaskItemSerialisierer(data=task)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskItemDetailView(APIView):
    """
    A class-based view for handling detailed operations on a TaskItem.

    Methods:
    - `get_object_or_404(self, pk)`: Retrieves a TaskItem instance by its primary key or raises a 404 error.

    - `delete(self, request, pk, format=None)`: Handles HTTP DELETE request to delete a TaskItem instance.

    - `put(self, request, pk, format=None)`: Handles HTTP PUT request to update a TaskItem instance.
    """

    def get_object_or_404(self, pk):
        """
        Retrieves a TaskItem instance by its primary key or raises a 404 error.

        Args:
            pk (int): The primary key of the TaskItem.

        Returns:
            TaskItem: The TaskItem instance.
        """
        return TaskItem.objects.get(pk=pk)

    def delete(self, request, pk, format=None):
        """
        Handles HTTP DELETE request to delete a TaskItem instance.

        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the TaskItem to be deleted.
            format (str, optional): The requested format for the response. Defaults to None.

        Returns:
            Response: A Response object with status HTTP_204_NO_CONTENT.
        """
        task = self.get_object_or_404(pk)
        print(task)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def put(self, request, pk, format=None):
        """
        <Handles HTTP<<<< PUT request to update a TaskItem instance.

        Args:
            request (HttpRequest): The HTTP request object.
            pk (int): The primary key of the TaskItem to be updated.
            format (str, optional): The requested format for the response. Defaults to None.

        Returns:
            Response: A Response object with the updated TaskItem data or error messages.
        """
        update_task = request.data.copy()
        task = self.get_object_or_404(pk)
        task.author = request.user.id
        serializer = TaskItemSerialisierer(task, data=update_task)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
