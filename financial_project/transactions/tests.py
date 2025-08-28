from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Account, Transaction, AuditLog

class UserRegistrationLoginTests(APITestCase):
    def test_user_registration(self):
        url = reverse('user_register')
        data = {
            "username": "testuser",
            "email": "testuser@example.com",
            "password": "testpass123",
            "password2": "testpass123"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().username, "testuser")

    def test_user_login(self):
        user = User.objects.create_user(username='testuser', password='testpass123')
        url = reverse('api_token_auth')
        data = {
            "username": "testuser",
            "password": "testpass123",
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue('token' in response.data)

class AccountAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='accountuser', password='password123', is_staff=True)
        self.client.force_authenticate(user=self.user)
        self.account_data = {
            "account_number": "1234567890",
            "account_name": "My Savings Account",
            "user": self.user.id,
            "account_type": "Savings",
            "balance": "1000.00"
        }

    def test_create_account(self):
        url = reverse('account-list')
        response = self.client.post(url, self.account_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['account_name'], "My Savings Account")

    def test_get_accounts(self):
        response = self.client.post(reverse('account-list'), self.account_data, format='json')
        url = reverse('account-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

class TransactionAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='transuser', password='password123', is_staff=True)
        self.client.force_authenticate(user=self.user)
        self.account = Account.objects.create(
            account_number="9876543210",
            account_name="Test Account",
            user=self.user,
            account_type="Checking",
            balance="2000.00"
        )
        self.transaction_data = {
            "account": self.account.id,
            "user": self.user.id,
            "transaction_id": "TXN10001",
            "transaction_type": "CR",
            "amount": "500.00",
            "category": "Salary",
            "description": "Salary credited",
            "status": "Completed",
            "remarks": ""
        }

    def test_create_transaction(self):
        url = reverse('transaction-list')
        response = self.client.post(url, self.transaction_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['transaction_id'], "TXN10001")

    def test_get_transactions(self):
        self.client.post(reverse('transaction-list'), self.transaction_data, format='json')
        url = reverse('transaction-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(len(response.data) > 0)

class AuditLogTests(APITestCase):
    def setUp(self):
        self.admin_user = User.objects.create_user(username='adminuser', password='pass123', is_staff=True)
        self.client.force_authenticate(user=self.admin_user)

    def test_audit_log_created_on_account_creation(self):
        url = reverse('account-list')
        data = {
            "account_number": "ACC123",
            "account_name": "Audit Test Account",
            "user": self.admin_user.id,
            "account_type": "Savings",
            "balance": "1000.00"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        created_id = response.data['id']
        logs = AuditLog.objects.filter(model_name='Account', object_id=created_id, action='CREATE')
        self.assertTrue(logs.exists())
        self.assertEqual(logs.first().changed_by, self.admin_user)
