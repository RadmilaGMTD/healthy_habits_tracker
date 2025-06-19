from django.urls import path

from habits.apps import HabitsConfig

from .views import (
    HabitCreateApiView,
    HabitDestroyApiView,
    HabitListApiView,
    HabitRetrieveApiView,
    HabitUpdateApiView,
    PublicHabitListApiView,
)

app_name = HabitsConfig.name


urlpatterns = [
    path("habits/create/", HabitCreateApiView.as_view(), name="habits_create"),
    path("habits/", HabitListApiView.as_view(), name="habits_list"),
    path("habits/public/", PublicHabitListApiView.as_view(), name="public_habits_list"),
    path("habits/<int:pk>/", HabitRetrieveApiView.as_view(), name="habits_get"),
    path("habits/update/<int:pk>/", HabitUpdateApiView.as_view(), name="habits_update"),
    path("habits/delete/<int:pk>/", HabitDestroyApiView.as_view(), name="habits_delete"),
]
