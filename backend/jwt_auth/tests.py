from django.test import TestCase
from django.urls import reverse
from rest_framework.response import Response


class JWTAuthTestCase(TestCase):
    user_data = {
        'username': 'test',
        'email': 'test@gmail.com',
        'password': 'test',
        # write only fields
        'is_staff': True,
        'date_joined': '2024-11-17 23:00:05.471492',
    }

    def get_user_info(self, access_token=None) -> Response:
        rsp = self.client.get(
            reverse('user-info'),
            headers=(
                None
                if access_token is None
                else {'Authorization': f'Bearer {access_token}'}
            ),
        )
        return rsp

    def test_user_registration_and_login(self):
        # register
        rsp = self.client.post(
            reverse('register-user'),
            self.user_data,
        )
        self.assertEqual(rsp.status_code, 201)

        # login
        rsp = self.client.post(
            reverse('user-login'),
            self.user_data,
        )
        self.assertEqual(rsp.status_code, 200)
        access = rsp.data['access']
        refresh = rsp.data['refresh']

        rsp = self.get_user_info(access)
        self.assertEqual(rsp.status_code, 200)
        self.assertNotIn('password', rsp.data)
        self.assertNotEqual(self.user_data['is_staff'], rsp.data['is_staff'])
        self.assertNotEqual(
            self.user_data['date_joined'],
            rsp.data['date_joined'],
        )

        # refresh access token
        rsp = self.client.post(
            reverse('refresh-token'),
            {'refresh': refresh},
        )
        self.assertEqual(rsp.status_code, 200)

        # get user info with new token
        new_access_token = rsp.data['access']
        rsp = self.get_user_info(new_access_token)
        self.assertEqual(rsp.status_code, 200)

    def test_get_user_info_without_credentials(self):
        rsp = self.get_user_info()
        self.assertEqual(rsp.status_code, 401)
