from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@londonappdev.com'
        password = 'Password123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        '''test a new users email is normalised'''
        email = 'test@HEkkdaksf.com'
        user = get_user_model().objects.create_user(email, "1234")
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        '''test creating users with no email address'''
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, '1345')

    def test_create_new_superuser(self):
        '''test creating a new super user'''
        user = get_user_model().objects.create_superuser(
            'test@test.con',
            '1234'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
