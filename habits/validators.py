from rest_framework.validators import ValidationError


class HabitValidator:

    def __call__(self, value):
        is_pleasant = value.get("is_pleasant", False)
        reward = value.get("reward")
        associated_habit = value.get("associated_habit")
        time_complete = value.get("time_complete")
        periodicity = value.get("periodicity", 1)

        if is_pleasant:
            if reward:
                raise ValidationError("Приятная привычка не может иметь вознаграждение")
            if associated_habit:
                raise ValidationError("Приятная привычка не может иметь связанную привычку")
        else:
            if reward and associated_habit:
                raise ValidationError("У полезной привычки должно быть или вознаграждение или приятная привычка")

        if associated_habit and not associated_habit.is_pleasant:
            raise ValidationError("Связанная привычка должна быть приятной (is_pleasant=True)")

        if time_complete:
            if time_complete.total_seconds() > 120:
                raise ValidationError("Время на выполнение должно быть не больше 120 секунд")

        if periodicity > 7:
            raise ValidationError("Нельзя не выполнять привычку более 7 дней")
