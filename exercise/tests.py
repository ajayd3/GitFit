from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from forum_app.views import forums_main 
from oauth_app.views import dashboard
from workouts_app.views import choices
from django.contrib import admin


# Create your tests here.

class DummyTestCase(TestCase):
    def setUp(self):
        x = 1  
    def test_dummy_test_case(self):
        self.assertEqual(1, 1)

class TestUrls(SimpleTestCase):
    def test_forum_url_is_resolved(self):
        url= reverse('forums')
        print(resolve(url))
        self.assertEquals(resolve(url).func, forums_main)
    def test_dash_url_is_resolved(self):
        url= reverse('dashboard')
        self.assertEquals(resolve(url).func, dashboard)
    def test_choices_url_is_resolved(self):
        url=reverse('workouts_main')
        self.assertEquals(resolve(url).func, choices)

    