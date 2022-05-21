from rest_framework import serializers

from .models import PRIOTRITY_CHOICES, REPEAT_CHOICES, Task, List

repeat_choices = REPEAT_CHOICES
priority_choices = PRIOTRITY_CHOICES

class TaskEditSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    task = serializers.CharField(min_length=1, max_length=64)
    owner = serializers.IntegerField()
    due = serializers.DateTimeField()
    priority = serializers.IntegerField()
    repeat = serializers.CharField(min_length=1, max_length=16),
    end_repeat = serializers.DateField()
    list = serializers.IntegerField()
    assigned = serializers

    def validate_repeat(self, value):
        if value not in repeat_choices:
            raise serializers.ValidationError("This is not a valid repeat interval.")
        return value

    def validate_priority(self, value):
        if value not in priority_choices:
            raise serializers.ValidationError("This is not a valid priority option.")
        return value


