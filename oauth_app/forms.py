from django import forms
from .models import Workouts
class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workouts
        fields = ["workout_type", "workout_difficulty", "workout_info"]

        widgets = {
            'workout_type': forms.TextInput(attrs={'class':'form-control'}),
            'workout_difficulty': forms.TextInput(attrs={'class':'form-control'}),
            'workout_info': forms.Textarea(attrs={'class':'form-control'}),
        }

