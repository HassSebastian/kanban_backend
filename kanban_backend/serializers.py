from rest_framework import serializers

from tasklist.models import TaskItem

class TaskItemSerialisierer(serializers.ModelSerializer):
    class Meta:
        model = TaskItem
        fields = '__all__'
        
