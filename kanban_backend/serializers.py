from rest_framework import serializers

from tasklist.models import Regist, TaskItem

class TaskItemSerialisierer(serializers.ModelSerializer):
    class Meta:
        model = TaskItem
        fields = '__all__'
        
class RegistListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Regist
        fields = '__all__'
        # extra_kwargs = {
        #     'color': {'required': False},
        #     'initials': {'required': False},
        # }