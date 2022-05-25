from rest_framework import serializers

from .models import PRIOTRITY_CHOICES, REPEAT_CHOICES, Task, List

repeat_choices = REPEAT_CHOICES
priority_choices = PRIOTRITY_CHOICES


class TaskEditSerializer(serializers.Serializer):
    owner = serializers.IntegerField()
    task = serializers.CharField(min_length=1, max_length=64, read_only=True)
    due = serializers.DateTimeField(read_only=True)
    priority = serializers.IntegerField()
    repeat = serializers.CharField(min_length=1, max_length=16, read_only=True)
    end_repeat = serializers.DateField(read_only=True)
    list = serializers.IntegerField(read_only=True)
    assigned = serializers.IntegerField(read_only=True)

    def validate_repeat(self, value):
        if value not in repeat_choices and value != None:
            raise serializers.ValidationError("This is not a valid repeat interval.")
        return value

    def validate_priority(self, value):
        if value not in priority_choices and value != None:
            raise serializers.ValidationError("This is not a valid priority option.")
        return value

    def validate_assigned(self, value):
        pass

    def validate_list(self, value):
        pass

class ListEditSerializer(serializers.Serializer):
    pass

