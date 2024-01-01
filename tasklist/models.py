import random
from django.contrib.auth.models import User
from django.db import models
from datetime import date


class Regist(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    color = models.IntegerField(null=True, blank=True)
    initials = models.CharField(max_length=2,null=True, blank=True)

    def save(self, *args, **kwargs):
        self.color = random.randint(0, 6)
        self.initials = self.first_name[0] + self.last_name[0]
        super().save(*args, **kwargs)
        
    def __str__(self):
        return f"{self.first_name} {self.last_name}"



class TaskItem(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200, blank=True, null=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,null=True
    )
    collaborator = models.ManyToManyField(
        User, blank=True, related_name="collaborated_tasks"
    )
    created_at = models.DateField(default=date.today)
    task_status = ((0, "To-do"), (1, "Do-today"), (2, "In-progress"), (3, "Done"))
    status = models.SmallIntegerField(choices=task_status, default=0)
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
        return f"({self.id}) {self.title}"

