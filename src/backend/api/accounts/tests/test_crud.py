from rest_framework.reverse import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.serializers import ModelSerializer
from ..models import Account
from .factories import AccountFactory

class AccountSerializer(ModelSerializer):
    class Meta:
        model = Account

class AccountTests(APITestCase):

    def test_create_account(self):
        u = AccountFactory.build(username="fakeuser")
        s = AccountSerializer(u)
        data = s.data
        data['confirm_password'] = data['password']

        url = reverse('accounts:account-list')
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Account.objects.count(), 1)
        self.assertNotEqual(Account.objects.get(id=1).password, 'superstrong')

    def test_create_invalid_user(self):
        url = reverse('accounts:account-list')
        u = AccountFactory.build(username="invalide user name")
        s = AccountSerializer(u)
        data = s.data

        data['confirm_password'] = data['password']

        # invalid username
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # invalid username length
        data['username'] = 'short'
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # password match
        data['username'] = 'validusername'
        data['confirm_password'] = "doesn't match"
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_duplicate_username(self):
        url = reverse('accounts:account-list')
        # exists username
        u = AccountFactory.create(username="testuser")
        s = AccountSerializer(u)
        data = s.data
        data['confirm_password'] = data['password']
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_user(self):
        u = AccountFactory.create(first_name="first_test")

        url = reverse('accounts:account-detail', args=[u.username])
        data = {'first_name': 'second_test'}

        response = self.client.patch(url, data)
        u.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(u.first_name, 'second_test')

    def test_delete_user(self):
        u = AccountFactory.create()

        url = reverse('accounts:account-detail', args=[u.username])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_full_name(self):
        u = AccountFactory.create()
        full = "{} {}".format(u.first_name, u.last_name)

        self.assertEqual(u.get_short_name(), u.first_name)
        self.assertEqual(u.get_full_name(), full)
