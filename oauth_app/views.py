from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout
from django.http import HttpResponse

from django.contrib.auth.models import User
from .models import UserProfile
from django.db import models

from .models import Workouts
from .forms import WorkoutForm

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse

from django.template import loader
from django.urls import reverse
from .models import Workouts
from django.views import generic
from django.db.models import F



def logout_view(request):
    logout(request)
# Create your views here.
def dashboard(request):
    context = {}
    if(UserProfile.objects.all().filter(user=request.user).count()==0):
        up = UserProfile(user = request.user, height=0, weight=0, fav_exer="", points=0)
        up.save()
    return render(request, 'dashboard.html', context)


def get_user_profile(request, username):
    if (User.username == username):
        user = User.objects.get(username=username)
        up = UserProfile.objects.get(user=user)
        return render(request, '/profile.html/', {"user":User})
    else:
        return render(
            request,
            'profile.html/'
        )

def submit_profile(request, username):
    if(request.method=="POST"):
        user = User.objects.get(username=username)
        up = UserProfile.objects.get(user=user)
        ##print(User.userprofile.weight)
        up.weight=request.POST['weight_field']
        up.height=request.POST['height_field']
        up.save()
    return redirect("/dashboard/profile/"+username+"/")

def get_or_create_user_profile(request):
    profile= None
    user= request.user
    try:
        profile=UserProfile.objects.get(user= request.user)
    except UserProfile.DoesNotExist:
        profile= UserProfile.objects.create(user= request.user, height=0, weight=0, fav_exer="", points=0)
    return profile 

def add_points(request):
    if request.POST.get('points_btn'):
        print("IN ADD POINTS FUNC ")
        #profil= UserProfile.objects.get(user=request.user)
        #profil= get_object_or_404(UserProfile, user=request.user)
        profil=get_or_create_user_profile(request)
        profil.points = F('points') + 10
        print(profil.points)
        profil.save()
    #return render(request, 'profile.html/')
    #return redirect("/dashboard/profile/"+username+"/")
    return redirect("/dashboard/")
    #return render(request, 'dashboard.html', context)





class WorkoutsView(generic.CreateView):
    template_name = 'new_workout.html'

    def get(self, request):
        form = WorkoutForm()
        print('Hello')
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = WorkoutForm(request.POST)
        if form.is_valid():
            form.save()
            text1 = form.cleaned_data['workout_type']
            text2 = form.cleaned_data['workout_difficulty']
            text3 = form.cleaned_data['workout_info']
            form = WorkoutForm()
            if (text1 == "cardio" or "running" or "run") and (text2.lower() == "easy"):
                redirect('workouts/cardio_easy')
            elif (text1 == "cardio" and text2.lower() == "moderate"):
                redirect('workouts/cardio_moderate')
            elif (text1 == "cardio" and text2.lower() == "difficult"):
                redirect('workouts/cardio_difficult')


            redirect('workouts/list')


def workouts(request):

    if request.POST.get('workout_type') is not None:
        workouts_list = Workouts.objects.all()
        workout_type = request.POST.get("workout_type")
        workout_difficulty = request.POST.get("workout_difficulty")
        workout_info = request.POST.get("workout_info")
        workout = Workouts(workout_type=workout_type, workout_difficulty=workout_difficulty, workout_info=workout_info)
        workout.save()
        # print(workout_type)
        # print(workout_type == "cardio")
        # print(workout_difficulty)
        # print(workout_difficulty == "moderate")


        workouts_list = Workouts.objects.all()
        cardio = workouts_list.filter(workout_type='Cardio') | workouts_list.filter(workout_type='cardio') \
                 | workouts_list.filter(workout_type='run') | workouts_list.filter(workout_type='running') \
                 | workouts_list.filter(workout_type='Running') | workouts_list.filter(workout_type='Run')


        cardio_easy = cardio.filter(workout_difficulty='easy') | cardio.filter(workout_difficulty='Easy')
        workouts_list = Workouts.objects.all()
        cardio = workouts_list.filter(workout_type='Cardio') | workouts_list.filter(workout_type='cardio') \
                 | workouts_list.filter(workout_type='run') | workouts_list.filter(workout_type='running') \
                 | workouts_list.filter(workout_type='Running') | workouts_list.filter(workout_type='Run')

        cardio_moderate = cardio.filter(workout_difficulty='moderate') | cardio.filter(workout_difficulty='medium') \
                          | cardio.filter(workout_difficulty='Moderate') | cardio.filter(workout_difficulty='Medium')
        workouts_list = Workouts.objects.all()
        cardio = workouts_list.filter(workout_type='Cardio') | workouts_list.filter(workout_type='cardio') \
                 | workouts_list.filter(workout_type='run') | workouts_list.filter(workout_type='running') \
                 | workouts_list.filter(workout_type='Running') | workouts_list.filter(workout_type='Run')


        cardio_hard = cardio.filter(workout_difficulty='difficult') | cardio.filter(workout_difficulty='Difficult') \
                    | cardio.filter(workout_difficulty='hard') | cardio.filter(workout_difficulty='Hard')
        workouts_list = Workouts.objects.all()
        cardio = workouts_list.filter(workout_type='Cardio') | workouts_list.filter(workout_type='cardio') \
                 | workouts_list.filter(workout_type='run') | workouts_list.filter(workout_type='running') \
                 | workouts_list.filter(workout_type='Running') | workouts_list.filter(workout_type='Run')

        # cardio check
        workouts_list = Workouts.objects.all()

        yoga = workouts_list.filter(workout_type='Yoga') | workouts_list.filter(workout_type='yoga') |\
                                                                                             workouts_list.filter(workout_type='home')
        workouts_list = Workouts.objects.all()
        yoga_easy = yoga.filter(workout_difficulty='easy') | yoga.filter(workout_difficulty='Easy')

        workouts_list = Workouts.objects.all()
        yoga = workouts_list.filter(workout_type='Yoga') | workouts_list.filter(workout_type='yoga') | \
               workouts_list.filter(workout_type='home')
        yoga_middle = yoga.filter(workout_difficulty='moderate') | yoga.filter(workout_difficulty='Moderate') | \
                      yoga.filter(workout_difficulty='medium') | yoga.filter(workout_difficulty='moderate')

        workouts_list = Workouts.objects.all()
        yoga = workouts_list.filter(workout_type='Yoga') | workouts_list.filter(workout_type='yoga') | \
               workouts_list.filter(workout_type='home')
        yoga_difficult = yoga.filter(workout_difficulty='difficult') | yoga.filter(workout_difficulty='Difficult')|\
                        yoga.filter(workout_difficulty='hard') | yoga.filter(workout_difficulty='Hard')

        workouts_list = Workouts.objects.all()
        lifting = workouts_list.filter(workout_type='weightlifting') | workouts_list.filter(workout_type='lifting' )|\
               workouts_list.filter(workout_type='Weightlifting') | workouts_list.filter(workout_type='Lifting')
        workouts_list = Workouts.objects.all()

        lifting_easy = lifting.filter(workout_difficulty='easy') | lifting.filter(workout_difficulty='Easy')
        workouts_list = Workouts.objects.all()
        lifting = workouts_list.filter(workout_type='weightlifting') | workouts_list.filter(workout_type='lifting' )|\
               workouts_list.filter(workout_type='Weightlifting') | workouts_list.filter(workout_type='Lifting')
        lifting_middle = lifting.filter(workout_difficulty='moderate') | lifting.filter(workout_difficulty='Moderate') | \
                      lifting.filter(workout_difficulty='medium') | lifting.filter(workout_difficulty='moderate')
        workouts_list = Workouts.objects.all()
        lifting = workouts_list.filter(workout_type='weightlifting') | workouts_list.filter(workout_type='lifting' )|\
               workouts_list.filter(workout_type='Weightlifting') | workouts_list.filter(workout_type='Lifting')
        lifting_difficult = lifting.filter(workout_difficulty='difficult') | lifting.filter(workout_difficulty='Difficult') | \
                            lifting.filter(workout_difficulty='hard') | lifting.filter(workout_difficulty='Hard')
        # print(workout_difficulty)

        if (workout.workout_type.lower() == "cardio" or "running" or "run"):
            print("HALALSDLFJDSF")
            if(workout.workout_difficulty.lower() == "easy"):
                if(workout.workout_type.lower() == "yoga" and workout_type != "cardio"):
                    context = {'workouts_list': yoga_easy}
                    return render(request, "workouts/yoga_easy.html", context)
                if ((workout.workout_type.lower() == "cardio" or "running" or "run") and workout_type!= "lifting"):
                    context = {'workouts_list': cardio_easy}
                    return render(request, "workouts/cardio_easy.html", context)
                if(workout.workout_type.lower() == "lifting" or "weightlifting"):
                    context = {'workouts_list': lifting_easy}
                    return render(request, "workouts/weightlifting_easy.html", context)

            elif (workout_difficulty == "moderate"or "medium") and (workout_difficulty != "hard"or "difficult"):
                if (workout.workout_type.lower() == "yoga" and workout_type != "cardio" and workout_difficulty!= "hard" and workout_difficulty!= "difficult" ):
                    context = {'workouts_list': yoga_middle}
                    return render(request, "workouts/yoga_moderate.html", context)
                if ((workout.workout_type.lower() == "cardio" or "running" or "run") and workout_type != "lifting" and workout_difficulty!= "difficult" and workout_difficulty != "hard" ):
                    context = {'workouts_list': cardio_moderate}
                    return render(request, "workouts/cardio_moderate.html", context)

            if ((workout.workout_type.lower() == "lifting" or "weightlifting") and (
                    workout_difficulty != "difficult" and workout_difficulty != "hard")):
                if (workout_difficulty != "hard" or "difficult"):
                    context = {'workouts_list': lifting_middle}
                    return render(request, "workouts/weightlifting_moderate.html", context)

        context = {'workouts_list': cardio_hard}
        if (workout.workout_type.lower() == "yoga" and workout_type != "cardio"):
            context = {'workouts_list': yoga_difficult}
            return render(request, "workouts/yoga_difficult.html", context)
        if ((workout.workout_type.lower() == "cardio" or "running" or "run") and workout_type != "lifting"):
            context = {'workouts_list': cardio_hard}
            return render(request, "workouts/cardio_difficult.html", context)
        if (workout.workout_type.lower() == "lifting" or "weightlifting"):
            context = {'workouts_list': lifting_difficult}
            return render(request, "workouts/weightlifting_difficult.html", context)
    return render(request, "workouts/cardio_difficult.html", context)
