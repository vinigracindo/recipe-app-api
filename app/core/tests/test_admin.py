"""
Tests for the Django admin modifcations.
"""
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):
    """Tests for Django admin."""

    def setUp(self):
        """Create user and client."""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='testpass123',
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email='user@example.com',
            password='testpass1234',
            name='Test user'
        )

    def test_user_list(self):
        """Test that users are listed on page."""
        url = reverse('admin:core_user_changelist')
        response = self.client.get(url)

        self.assertContains(response, self.user.name)
        self.assertContains(response, self.user.email)

    def test_edit_user_page(self):
        """Test the edit user page works."""
        url = reverse('admin:core_user_change', args=[self.user.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_create_user_page(self):
        """Test the create user page works."""
        url = reverse('admin:core_user_add')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
