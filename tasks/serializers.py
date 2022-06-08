
from rest_framework import serializers

from .models import PRIORITY_CHOICES, REPEAT_CHOICES, Task, List

repeat_choices = REPEAT_CHOICES
priority_choices = PRIORITY_CHOICES


class TaskEditSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    owner = serializers.IntegerField(read_only=True)
    task = serializers.CharField(max_length=64, required=True)
    due = serializers.DateField(required=False, allow_null=True)
    priority = serializers.ChoiceField(choices=priority_choices, required=False, allow_null=True)
    repeat = serializers.ChoiceField(choices=repeat_choices, required=False, allow_null=True)
    end_repeat = serializers.DateField(required=False, allow_null=True)
    #assigned = serializers.
    #list = 


    def update(self, instance, validated_data):
        instance.task = validated_data.get('task', instance.task)
        instance.due = validated_data.get('due', instance.due)
        instance.priority = validated_data.get('priority', instance.priority)
        instance.repeat = validated_data.get('repeat', instance.repeat)
        instance.end_repeat = validated_data.get('end_repeat', instance.end_repeat)
        #instance.assigned = validated_data.get('assigned', instance.assigned)
        #instance.list = validated_data.get('list', instance.list)
        instance.save()
        return instance



class ListEditSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user = serializers.IntegerField(read_only=True)
    list = serializers.CharField(max_length=64, required=True)


    def update(self, instance, validated_data):
        instance.list = validated_data.get('list', instance.list)
        instance.save()
        return instance


class ListSerializer(serializers.ModelSerializer):

    class Meta:
        model = List
        fields = ['id', 'list', 'user']


class TaskSerializer(serializers.ModelSerializer):

    list = ListSerializer()

    class Meta:
        model = Task
        fields = ['id', 'owner', 'task', 'created', 'due', 'completed', 'priority', 'repeat', 'end_repeat', 'list']




