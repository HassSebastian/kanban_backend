from django.db import models
from django.contrib.auth.models import User
from datetime import date





class TaskItem(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=200, blank=True, null=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
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
        return f'({self.id}) {self.title}'
    
    
