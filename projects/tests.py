from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from rest_framework import status


class AllPeopleTestCase(APITestCase):
    def test_all_people_is_online(self):
        response = self.client.get(reverse("people"))

        self.assertEqual(response.status_code, status.HTTP_200_OK)
