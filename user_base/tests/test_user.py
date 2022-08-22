from django.test import Client
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.core import mail


class CreationUserTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.username = 'test'
        self.password1 = '1234azerty56789'
        self.email = 'testuser@email.com'

    def test_user(self):
        response = self.client.get(reverse('sign_up'))
        self.assertEqual(response.status_code, 200)
        credential = self.client.post(
            '/user_base/sign_up/',
            {
                'username': self.username,
                'email': self.email,
                'password1': self.password1,
                'password2': self.password1,
            }
        )
        self.assertEqual(credential.status_code, 302)
        user = User.objects.all()
        self.assertEqual(user.count(), 1)
        login = self.client.post(reverse('log_in'), data={
            'email': self.email,
            'password': self.password1,
        })
        self.assertEqual(login.status_code, 302)


class LoginTest(TestCase):

    def setUp(self):
        user = User.objects.create_user(
            email="email@email.com",
            username="test",
            password="1234azerty56789",
        )
        user.save()

    def test_login_view(self):
        response = self.client.get(reverse('log_in'))
        self.assertEqual(response.status_code, 200)
        credential = self.client.post(reverse('log_in'), data={
            'email': 'email@email.com',
            'password': '1234azerty56789',
        })
        self.assertEqual(credential.status_code, 302)


class ResetPasswordTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user(
            email="email@email.com",
            username="test",
            password="1234azerty56789",
        )
        self.user.save()

    def test_reset_password(self):
        response = self.client.get(reverse('password_reset'))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse(
            'password_reset'),
            data={
                'email': 'email@email.com',
            }
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(len(mail.outbox), 1)
        self.assertRedirects(response, '/user_base/password_reset/done/')

        token = response.context['token']
        uid = response.context['uid']
        response = self.client.get(reverse(
            'password_reset_confirm',
            kwargs={'token': token, 'uidb64': uid}
        ))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, f'/user_base/password-reset-confirm/{uid}/set-password/')

        response = self.client.post(
            reverse(
                'password_reset_confirm',
                kwargs={'token': token, 'uidb64': uid}),
            {'new_password1': 'pass', 'new_password2': 'pass'}
        )
        self.assertEqual(response.status_code, 302)
