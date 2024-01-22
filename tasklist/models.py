import random
from django.contrib.auth.models import User
from django.db import models
from datetime import date
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class TaskItem(models.Model):
    """
    Model for tasks.

    Fields:
    - `title` (CharField): The title of the task with a maximum length of 50 characters.
    - `description` (CharField, optional): The description of the task with a maximum length of 200 characters.
    - `author` (ForeignKey): The author of the task, a reference to the user model (`settings.AUTH_USER_MODEL`).
    - `collaborator` (ManyToManyField): Collaborators on the task, a reference to the user model.
    - `created_at` (DateField): The date when the task was created, with the default value set to today's date.
    - `status` (SmallIntegerField): The status of the task, chosen from predefined options ('To-do', 'Do-today', 'In-progress', 'Done').
    - `due_date` (DateField, optional): The due date of the task.
    - `color` (SmallIntegerField): The color of the task, chosen from predefined options ('Yellow', 'Blue', 'Green', 'Orange', 'Red', 'Cyan', 'Purple').

    Methods:
    - `__str__(self)`: Returns a readable string representation of the task.
    """
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True, null=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="authored_tasks",
        null=True,
    )
    collaborator = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="collaborated_tasks", blank=True
    )
    created_at = models.DateField(default=date.today)
    task_status = ((0, "To-do"), (1, "Do-today"), (2, "In-progress"), (3, "Done"))
    status = models.SmallIntegerField(choices=task_status, default=0)
    due_date = models.DateField(blank=True, null=True)
    task_color = (
        (0, "Yellow"),
        (1, "Blue"),
        (2, "Green"),
        (3, "Orange"),
        (4, "Red"),
        (5, "Cyan"),
        (6, "Purple"),
    )
    color = models.SmallIntegerField(choices=task_color, default=0)

    def __str__(self):
        """
        Returns a readable string representation of the task.

        Returns:
        str: A string in the format "(ID) Title".
        """
        return f"({self.id}) {self.title}"
