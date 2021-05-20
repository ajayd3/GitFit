from django.test import TestCase
from .models import Forum, ForumPost
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.urls import reverse


# Create your tests here.

class ForumTestCase(TestCase):
    def setUp(self):
        Forum.objects.create(title="New Test Forum!", time_started=timezone.now(), description="This is purely for testing only")
        f = Forum.objects.get(title="New Test Forum!")
        user = User.objects.create_user(username='john',
                                 email='jlennon@beatles.com',
                                 password='glass onion')
        ForumPost.objects.create(text="First forum post to new test forum!", time_posted=timezone.now(), user=user, forum=f)
    def test_forum_object_created(self):
        f = Forum.objects.get(title="New Test Forum!")
        self.assertEqual(f.description, 'This is purely for testing only')
        u=User.objects.get(email='jlennon@beatles.com')
        fp = ForumPost.objects.get(text="First forum post to new test forum!")
        self.assertEqual(fp.user, u)
        self.assertEqual(fp.forum, f)
        self.assertEqual(fp.text, "First forum post to new test forum!")
    
    def testNoDuplicateForums(self):
        with self.assertRaises(Exception) as raised:
            f1=Forum.objects.create(title="no clones allowed", description="you better not clone me!")
            f2=Forum(title="no clones allowed", description="you better not clone me!")
            f2.save()
        self.assertEqual(IntegrityError, type(raised.exception))

class TestForumUrl(TestCase):
    def test_forum_url_list_display_is_resolved(self):
        url = reverse('forums')
        self.assertEqual(url, '/forums/')
    def test_forum_url_is_resolved(self):
        f=Forum(title="testing testing test", description="testerino neighberino")
        f.save()
        url=reverse('forum_display', args=[f.id])
        i=f.id
        literal_url="/forums/"+str(i)+"/"
        self.assertEqual(url, literal_url)           