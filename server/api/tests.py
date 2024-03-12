from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.management import call_command
from api.models import *


class AreaTest(APITestCase):
    main_url = reverse('area-list-create')
    detail_url = reverse('area-detail', args=[1])

    @classmethod
    def setUpTestData(cls):
        User.objects.create_user('johndoe', 'john@example.com', 'password')
        call_command('load_factories')

    def setUp(self):
        self.user = User.objects.get(username='johndoe')
        response = self.client.post(reverse('token_obtain_pair'), {
            "username": "johndoe",
            "password": "password",
        })
        self.token = response.data['access']

    def test_register_user(self):
        res_data = self.client.get(reverse('area-list-create'), HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(res_data.status_code, 200)

        # get all users records
        db_data = Area.objects.all().filter(owner_id=self.user.id)
        self.assertEqual(len(res_data.data), len(db_data))

        for i in range(len(res_data.data)):
            self.assertEqual(res_data.data[i]['name'], db_data[i].name)
