from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

class AuthTests(APITestCase):
    def test_register_and_login(self):
        r = self.client.post(reverse("register"), {"username":"alice","password":"secret12345"})
        self.assertEqual(r.status_code, status.HTTP_201_CREATED)

        r2 = self.client.post(reverse("login"), {"username":"alice","password":"secret12345"})
        self.assertEqual(r2.status_code, status.HTTP_200_OK)
        self.assertIn("access", r2.data)
