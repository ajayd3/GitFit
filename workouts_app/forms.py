from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit 
from .models import WorkoutRoutines

EXERCISE_CHOICES= [
    ('cardio', 'Cardio'),
    ('strength', 'Strength'),
    ('yoga', 'Yoga'),
    ]

class StartForm(forms.Form):
    #age= forms.IntegerField()
    #name= forms.CharField(label='Name')
    #ex_type= forms.CharField(label='What type of workouts would you like to see?', widget=forms.RadioSelect(choices=EXERCISE_CHOICES))
    ex_type= forms.CharField(label='What workout do you want to do?', widget=forms.Select(choices=[('cardio', 'Cardio'), ('strength', 'Strength'), ('yoga', 'Yoga')]))
    
    ex_diff= forms.CharField(label='What level of difficulty would you like?', widget=forms.Select(choices=[('easy', 'Easy'), ('medium', 'Medium'), ('hard', 'Hard')]))

    def __init__(self, *args, **kwargs):
        #ex_type = kwargs.pop('ex_type', None)
        #super(StartForm, self).__init__(*args, **kwargs)
        super().__init__(*args, **kwargs)
        self.helper=FormHelper
        self.helper.form_method= 'post'

        self.helper.layout= Layout(
            'ex_type',
            'ex_diff',
            Submit('submit', 'Submit', css_class='btn-success')
        )

class NewWorkoutForm(forms.ModelForm):
    class Meta:
        model = WorkoutRoutines
        fields = ["workout_title","workout_type", "workout_length","workout_difficulty", "workout_info"]

        widgets = {
            'workout_type': forms.Select(choices=["cardio","strength","yoga"]),
            'workout_difficulty': forms.Select(choices=["easy","medium","hard"]),
            'workout_info': forms.Textarea(attrs={'class':'form-control'}),
            'workout_length': forms.NumberInput(),
            'workout_title': forms.TextInput()
            
        }


