from rest_framework import serializers

from tasklist.models import TaskItem


class TaskItemSerialisierer(serializers.ModelSerializer):
    """
    Serializer class for TaskItem model.

    Fields:
    - `id` (int): The unique identifier for the task.
    - `title` (str): The title of the task.
    - `description` (str): The description of the task.
    - `author` (int): The ID of the author of the task.
    - `collaborator` (list): List of IDs of collaborators on the task.
    - `created_at` (str): The date when the task was created.
    - `status` (int): The status of the task.
    - `due_date` (str): The due date of the task.
    - `color` (int): The color code associated with the task.

    """
    class Meta:
        model = TaskItem
        fields = "__all__"
