from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from .models import Habit
from .paginators import HabitsPaginator
from .permissions import IsOwner, IsPublicOrIsOwner
from .serializers import HabitSerializer, PublicHabitSerializer


class HabitCreateApiView(generics.CreateAPIView):
    serializer_class = HabitSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class HabitListApiView(generics.ListAPIView):
    serializer_class = PublicHabitSerializer
    queryset = Habit.objects.all()
    pagination_class = HabitsPaginator
    permission_classes = [IsPublicOrIsOwner]

    def get_queryset(self):
        user_habits = Habit.objects.filter(user=self.request.user)
        public_habits = Habit.objects.filter(is_public=True)
        return user_habits | public_habits


class HabitRetrieveApiView(generics.RetrieveAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
    lookup_field = "pk"

    def get_serializer_class(self):
        if getattr(self, "swagger_fake_view", False):
            return HabitSerializer
        if self.get_object().user == self.request.user:
            return HabitSerializer
        return PublicHabitSerializer


class HabitUpdateApiView(generics.UpdateAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]


class HabitDestroyApiView(generics.DestroyAPIView):
    serializer_class = HabitSerializer
    queryset = Habit.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
