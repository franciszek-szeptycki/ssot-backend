from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.management import call_command


class JWTAccessTest(APITestCase):

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user(username='johndoe', password='password', email="john@doe.com")
        call_command("load_factories")

    def setUp(self):
        res = self.client.post(reverse('token_obtain_pair'), {
            'username': 'johndoe',
            'password': 'password',
        })
        self.token = res.data['access']

    def test_increment_order(self):
        pass
