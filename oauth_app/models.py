from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
  


# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #birth_date = models.DateField(null=True, blank=True)
    weight = models.CharField(max_length=50, blank=True)
    height = models.CharField(max_length=50, blank=True)
    fav_exer = models.TextField(max_length=100, blank=True)
    points= models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.user.username
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['user'], name='duplicate users in model not allowed')
        ]


class Workouts(models.Model):
    workout_type = models.CharField(max_length=100, null=False, blank=False)
    workout_difficulty = models.CharField(max_length=100, null=False, blank=False)
    workout_info = models.CharField(max_length=1000, null=False, blank=False)
