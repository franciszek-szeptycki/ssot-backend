from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User


class UserRegisterTest(APITestCase):

    def tearDown(self):
        User.objects.all().delete()

    url = reverse('register_user')

    def test_register_user(self):
        data = {
            "username": "testuser",
            "password": "testpassword",
            "email": "test@test.com",
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.get().username, data['username'])
        self.assertEqual(User.objects.get().email, data['email'])
        self.assertTrue(User.objects.get().check_password(data['password']))
        self.assertEqual(User.objects.count(), 1)

    def test_empty_fields(self):
        response = self.client.post(self.url, {})
        self.assertEqual(response.status_code, 400)

        phrase = 'This field is required.'
        self.assertEqual(response.data['username'][0], phrase)
        self.assertEqual(response.data['email'][0], phrase)
        self.assertEqual(response.data['password'][0], phrase)
        self.assertEqual(User.objects.count(), 0)

    def test_short_fields(self):
        response = self.client.post(self.url, {
            "username": "user",
            "password": "pass",
        })
        self.assertEqual(response.status_code, 400)

        phrase = lambda x: f"Ensure this field has at least {x} characters."
        self.assertEqual(response.data['username'][0], phrase(5))
        self.assertEqual(response.data['password'][0], phrase(8))
        self.assertEqual(User.objects.count(), 0)

    def test_invalid_email(self):
        response = self.client.post(self.url, {
            "username": "user",
            "password": "password123",
            "email": "invalidemail"
        })
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['email'][0], 'Enter a valid email address.')
        self.assertEqual(User.objects.count(), 0)

    def test_existing_user(self):
        response = None
        for _ in range(2):
            response = self.client.post(self.url, {
                "username": "test1",
                "password": "test1234",
                "email": "user@test.com"
            })

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['username'][0], 'Username already exists')
        self.assertEqual(response.data['email'][0], 'Email already exists')
        self.assertEqual(User.objects.count(), 1)

