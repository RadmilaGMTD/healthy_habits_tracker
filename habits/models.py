from django.db import models
from config import settings

class Habit(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Создатель привычки", null=True, blank=True
    )
    place = models.CharField(max_length=200, verbose_name="Место выполнения привычки")
    time = models.TimeField(verbose_name="Время, когда необходимо выполнять привычку")
    action = models.CharField(max_length=200, verbose_name="Действие, которое представляет собой привычка")
    is_pleasant = models.BooleanField(default=False, verbose_name="Признак приятной привычки")
    associated_habit = models.ForeignKey(
        'self', on_delete=models.SET_NULL, verbose_name="Связанная привычка", null=True, blank=True
    )
    periodicity = models.PositiveIntegerField(default=1, verbose_name="Периодичность", null=True, blank=True)
    reward = models.TextField(null=True, blank=True, verbose_name="Вознаграждение")
    time_complete = models.DurationField(verbose_name="Время на выполнение")
    is_public = models.BooleanField(default=False, verbose_name="Признак публичности")


    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

    def __str__(self):
        return f"{self.action} в {self.time} ({self.place})"
