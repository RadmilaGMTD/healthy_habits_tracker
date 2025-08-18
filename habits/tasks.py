from datetime import datetime

from celery import shared_task
from django.utils import timezone

from .models import Habit
from .services import send_telegram_message


@shared_task()
def send_reminder_habits():
    now = timezone.now()
    current_time = now.time()

    habits = Habit.objects.select_related("user").filter(user__tg_chat_id__isnull=False)

    for habit in habits:
        habit_time = (datetime.min + habit.time).time()
        if habit_time.hour == current_time.hour and habit_time.minute == current_time.minute:
            message = f"Напоминание: {habit.action} в {habit_time.strftime('%H:%M')}"
            send_telegram_message(habit.user.tg_chat_id, message)
