from django.db import models
from datetime import datetime
from django.utils import timezone
from oauth_app.models import UserProfile
from django.contrib.auth.models import User

# Create your models here.
class Forum(models.Model):
    title = models.CharField(max_length=100)
    time_started = models.DateTimeField(default=timezone.now(), blank=True)
    description = models.CharField(max_length=1000)
    def __str__(self):
        return self.title + " created on "+self.time_started.strftime("%Y-%m-%d %H:%M:%S")
    class Meta:
        unique_together = ["title", "description"]

class ForumPost(models.Model):
    text = models.CharField(max_length=1000)
    time_posted = models.DateTimeField(default=timezone.now(), blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #forum = models.ForeignKey(Forum, on_delete = models.CASCADE)
    forum = models.ForeignKey(Forum, on_delete = models.CASCADE)
    def __str__(self):
        return self.user.username+" posted on "+str(self.forum)+" at "+self.time_posted.strftime("%Y-%m-%d %H:%M:%S")
