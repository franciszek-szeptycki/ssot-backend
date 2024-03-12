from rest_framework.test import APITestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.management import call_command
from api.models import *


class AreaTest(APITestCase):
    area_url = reverse('area-list-create')
    area_url_details = lambda x: reverse('area-detail', args=[x])

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

    def test_get_area_list(self):
        res_data = self.client.get(self.area_url, HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(res_data.status_code, 200)

        # get all users records
        db_data = Area.objects.all().filter(owner_id=self.user.id)
        self.assertEqual(len(res_data.data), len(db_data))

        for i in range(len(res_data.data)):
            self.assertEqual(res_data.data[i]['name'], db_data[i].name)

    def test_get_area_detail(self):
        res_data = self.client.get(self.area_url_details(1), HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(res_data.status_code, 200)

        db_data = Area.objects.get(id=1)
        self.assertEqual(res_data.data['name'], db_data.name)

    def test_create_area(self):
        data = {
            "name": "Lorem",
            "is_open": True,
            "order": 1
        }
        res_data = self.client.post(self.area_url, data, HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(res_data.status_code, 201)

        db_data = Area.objects.get(name="Lorem")
        self.assertEqual(db_data.name, data['name'])
        self.assertEqual(db_data.is_open, data['is_open'])
        self.assertEqual(db_data.order, data['order'])


    def test_update_area(self):
        data = {
            "name": "Test Area",
            "is_open": True,
            "order": 1
        }
        res_data = self.client.put(self.area_url_details(1), data, HTTP_AUTHORIZATION=f'Bearer {self.token}')
        self.assertEqual(res_data.status_code, 200)

        db_data = Area.objects.get(id=1)
        self.assertEqual(db_data.name, data['name'])
        self.assertEqual(db_data.is_open, data['is_open'])
        self.assertEqual(db_data.order, data['order'])

    # def test_delete_area(self):
    #     db_before = Area.objects.all().filter(owner_id=self.user.id).order_by('id')
    #     res_data = self.client.delete(reverse("area-detail", args=[db_before.first().id]), HTTP_AUTHORIZATION=f'Bearer {self.token}')
    #     db_after = Area.objects.all().filter(owner_id=self.user.id)
    #
    #     self.assertEqual(res_data.status_code, 204)
    #     self.assertEqual(len(db_before), len(db_after) + 1)
