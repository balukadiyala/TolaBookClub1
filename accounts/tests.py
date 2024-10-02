from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class SignUpViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.signup_url = reverse('signup')

    def test_signup_post_with_valid_data(self):
        response = self.client.post(self.signup_url, {
            'email': 'test@example.com',
            'password': 'Password123!'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('Please confirm your email address to complete the registration.', response.content.decode())
        user = User.objects.get(email='test@example.com')
        self.assertFalse(user.is_active)  # User should not be active until email is verified

    def test_signup_post_with_invalid_password(self):
        response = self.client.post(self.signup_url, {
            'email': 'test@example.com',
            'password': 'pass'
        })
        self.assertEqual(response.status_code, 400)
        self.assertIn('Password must be at least 8 characters long and include numbers and symbols.', response.content.decode())

class EmailVerificationTestCase(TestCase):
    def test_email_verification(self):
        user = User.objects.create_user(username='test@example.com', email='test@example.com', password='Password123!', is_active=False)
        user.save()
        # Simulate clicking the verification link
        verification_url = reverse('email-verify') + '?token=some-token'
        response = self.client.get(verification_url)
        user.refresh_from_db()
        self.assertTrue(user.is_active)  # User should be active after verification