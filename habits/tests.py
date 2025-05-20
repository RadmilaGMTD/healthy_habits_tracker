from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User

from .models import Habit


class MaterialsTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email="test_user@mail.ru")
        self.habit = Habit.objects.create(
            user=self.user, place="Тестовое место", time="15:00:00", action="Тестовая привычка", time_complete="50"
        )
        self.client.force_authenticate(user=self.user)

    def test_retrieve_habit(self):
        response = self.client.get(f"/habits/{self.habit.pk}/")
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("action"), self.habit.action)

    def test_create_habit(self):
        data = {
            "place": "Тестовое место 2",
            "time": "15:00:00",
            "action": "Тестовая привычка 2",
            "time_complete": "50",
        }
        response = self.client.post("/habits/create/", data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_update_habit(self):
        data = {
            "place": "Тестовое место 3",
            "time": "15:00:00",
            "action": "Тестовая привычка 3",
            "time_complete": "50",
        }
        response = self.client.patch(f"/habits/update/{self.habit.pk}/", data)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("action"), "Тестовая привычка 3")

    def test_delete_habit(self):
        response = self.client.delete(f"/habits/delete/{self.habit.pk}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_list_habit(self):
        response = self.client.get("/habits/")
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            data,
            {
                "count": 1,
                "next": None,
                "previous": None,
                "results": [{"id": 4, "place": "Тестовое место", "action": "Тестовая привычка", "is_pleasant": False}],
            },
        )
