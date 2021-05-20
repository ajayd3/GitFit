from django.test import TestCase

# Create your tests here.
# from django.db import models
from .models import WorkoutRoutines
from django.test import TestCase
# import WorkoutRoutines
from .forms import StartForm, NewWorkoutForm
from django import forms
from django.db import IntegrityError
from workouts_app.views import get_workout_routine
from django.shortcuts import render, redirect
from django.urls import reverse

# Create your tests here.
class WorkoutTestCase(TestCase):
    def tescase1(self):
        testWorkout = WorkoutRoutines.objects.create(workout_title = "this workout is fun!", workout_type = "cardio", workout_difficulty = "easy", workout_info="run for 5 minutes", workout_length = 5)
        x = WorkoutRoutines.objects.get(workout_title="this workout is fun!")
        self.assertEqual(x.workout_title, "this workout is fun!")
        self.assertEqual(x.workout_type, "cardio")
        self.assertEqual(x.workout_difficulty, "easy")
        self.assertEqual(x.workout_info, "run for 5 minutes")
        self.assertEqual(x.workout_length, 5)

    def testcase2(self):
        testWorkout2 = WorkoutRoutines.objects.create(workout_title = "this workout is boring!", workout_type = "yoga", workout_difficulty = "hard", workout_info="do yoga for 15 minutes")
        x = WorkoutRoutines.objects.get(workout_title="this workout is boring!")
        self.assertEqual(x.workout_title, "this workout is boring!")
        self.assertEqual(x.workout_type, "yoga")
        self.assertEqual(x.workout_difficulty, "hard")
        self.assertEqual(x.workout_info, "do yoga for 15 minutes")
        self.assertEqual(x.workout_length, 0)


    def testcase3(self):
        testWorkout3 = WorkoutRoutines.objects.create(workout_title = "this workout is okay!", workout_type = "strength", workout_difficulty = "medium", workout_info="do lifting for 15 minutes")
        x = WorkoutRoutines.objects.get(workout_title="this workout is okay!")
        self.assertEqual(x.workout_title, "this workout is okay!")
        self.assertEqual(x.workout_type, "strength")
        self.assertEqual(x.workout_difficulty, "medium")
        self.assertEqual(x.workout_info, "do lifting for 15 minutes")
        self.assertEqual(x.workout_length, 0)
    
    def testNoDuplicateWorkouts(self):
        with self.assertRaises(Exception) as raised:
            w1=WorkoutRoutines.objects.create(workout_title="no clones allowed", workout_info="you better not clone me!")
            w2=WorkoutRoutines(workout_title="no clones allowed", workout_info="you better not clone me!")
            w2.save()
        self.assertEqual(IntegrityError, type(raised.exception))
    

    

class TestStartForm:
    def test_startform(self):
        form = StartForm()
        assertEqual(false, form.is_valid())
        data= {
            "ex_type": 'run',
            "ex_diff": 'easy'
        }
        form= StartForm(data=data)
        self.assertEqual(true, form.is_valid())

    
class TestNewWorkoutForm(forms.ModelForm):
    def test_new_work_form(self):
        form=NewWorkoutForm()
        assertEqual(false, form.is_valid())
        data={
            "workout_title": "my title",
            "workout_type": "cardio",
            "workout_length": 2,
            "workout_difficulty": "easy",
            "workout_info": "Sprint for 3 hours",
        }
        form=NewWorkoutForm(data= data)
        self.assertEqual(true, form.is_valid)
class TestWorkoutUrl(TestCase):
    def test_workout_url_list_display_is_resolved(self):
        url = reverse('workout_list_display', args=["cardio","easy"])
        self.assertEqual(url, '/workoutroutines/cardio/easy/')
    def test_workout_url_is_resolved(self):
        w=WorkoutRoutines(workout_title="testing testing test", workout_info="testerino neighberino")
        w.save()
        url=reverse('workout_display', args=[w.id])
        i=w.id
        literal_url="/workoutroutines/"+str(i)+"/"
        self.assertEqual(url, literal_url)