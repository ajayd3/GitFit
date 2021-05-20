from django.db import models

# Create your models here.
class WorkoutRoutines(models.Model):
    workout_title = models.CharField(max_length=100, null=False, blank=False)
    workout_type = models.CharField(max_length=100, null=False, blank=False, choices=(
            ("cardio","cardio"),
            ("strength","strength"),
            ("yoga","yoga")
        ))
    workout_difficulty = models.CharField(max_length=100, null=False, blank=False, choices=(
            ("easy","easy"),
            ("medium","medium"),
            ("hard","hard")
        ))
    workout_info = models.CharField(max_length=10000, null=False, blank=False)
    workout_length = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.workout_title+" type: "+self.workout_type
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['workout_title', 'workout_info'], name='duplicate workout title and info not allowed for workouts model')
        ]