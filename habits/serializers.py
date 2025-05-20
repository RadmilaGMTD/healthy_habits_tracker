from rest_framework import serializers

from .models import Habit
from .validators import HabitValidator


class HabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        validators = [HabitValidator()]
        read_only_fields = ("user",)


class PublicHabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ["id", "place", "action", "is_pleasant"]
        read_only_fields = fields
