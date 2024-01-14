from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model

User = get_user_model()


class AccountTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.register_url = reverse('account:register')
        self.login_url = reverse('account:login')
        self.user_list_url = reverse('account:user-list')
        self.user_detail_url = reverse('account:user-detail', args=[1])
        self.logout_url = reverse('account:logout')

        self.user_data = {
            'username': 'Bagyshan',
            'email': 'bagishan01@gmail.com',
            'phone_number': '+996709324447',
            'password': '120176saikal',
            'password_confirmation': '120176saikal'
        }
        self.login_data = {
            'email': 'bagishan01@gmail.com',
            'password': '120176saikal'
        }

        self.user = User.objects.create_user(**self.user_data)
        self.client.force_authenticate(user=self.user)

    def test_user_registration(self):
        response = self.client.post(self.register_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # def test_user_login(self):
    #     response = self.client.post(self.login_url, self.login_data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertIn('token', response.data)

    # def test_user_logout(self):
    #     response = self.client.post(self.logout_url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_user_list(self):
    #     response = self.client.get(self.user_list_url)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_user_detail(self):
    #     response = self.client.patch(self.user_detail_url, {'email': 'bagishan@gmail.com'}, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)