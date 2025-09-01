from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Recipe

class RecipeTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="bob", password="secret12345")
        # login to get token
        t = self.client.post(reverse("login"), {"username":"bob","password":"secret12345"}).data["access"]
        self.auth = {"HTTP_AUTHORIZATION": f"Bearer {t}"}

    def test_create_and_filter(self):
        # create
        r = self.client.post("/recipes/", {
            "title":"Omelette",
            "description":"tasty",
            "ingredients":"egg, salt, butter",
            "steps":"whisk and cook",
            "category":"breakfast",
        }, **self.auth)
        self.assertEqual(r.status_code, status.HTTP_201_CREATED)

        # list by ingredient
        r2 = self.client.get("/recipes/?ingredient=egg")
        self.assertEqual(r2.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(r2.data["count"], 1)

        # filter by category
        r3 = self.client.get("/recipes/?category=breakfast")
        self.assertEqual(r3.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(r3.data["count"], 1)
