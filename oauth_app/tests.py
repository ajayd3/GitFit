from django.test import TestCase
from django.contrib.auth.models import User
from oauth_app.models import UserProfile
from django.db import IntegrityError


class UserTestCase(TestCase):
    def setUp(self):
        user = User.objects.create_user(username='john',
        email='jlennon@beatles.com',
        password='glass onion')
        up = UserProfile.objects.create(user=user, weight=140, height=72, fav_exer="running", points=20)
    
    def test_userprofile_created(self):
        user = User.objects.get(email='jlennon@beatles.com')
        up = UserProfile.objects.get(user=user)
        self.assertEqual(up.user, user)
        self.assertEqual(up.weight, '140')
        self.assertEqual(up.height, '72')
        self.assertEqual(up.fav_exer, "running")
        self.assertEqual(up.points, 20)
    
    def test_duplicate_user_profile(self):
        with self.assertRaises(Exception) as raised:
            user = User.objects.create_user(username='john',
            email='jlennon@beatles.com',
            password='glass onion')
            up_1 = UserProfile.objects.create(user=user, weight=140, height=72)
            up_2 = UserProfile.objects.create(user=user, weight=149, height=77)
        self.assertEqual(IntegrityError, type(raised.exception))
# Create your tests here.
