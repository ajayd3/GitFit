from django.shortcuts import render
from .models import WorkoutRoutines
from .forms import NewWorkoutForm
from .forms import StartForm
from django.shortcuts import render, redirect
from django.views import generic


# Create your views here.
def get_workout_routine(request, workout_routine_id):
    w=WorkoutRoutines.objects.get(id=workout_routine_id)
    context = {"wr" : w}
    return render(request, 'workout.html', context)

def get_workout_list(request, type_id, diff_id):
    workout_list = WorkoutRoutines.objects.filter(workout_type=type_id, workout_difficulty=diff_id)
    print("workout_list: ")
    print(workout_list)
    context = {"diff":diff_id.capitalize(), "type":type_id.capitalize(),"workout_list":workout_list}
    return render(request,'workoutlist.html',context)

class WorkoutRoutinesView(generic.CreateView):
    template_name = 'new_workout_routine.html'

    def get(self, request):
        form = NewWorkoutForm()
        print('Hello')
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = NewWorkoutForm(request.POST)
        if form.is_valid():
            form.save()
            w_title = form.cleaned_data['workout_title']
            w_type = form.cleaned_data['workout_type']
            w_length = form.cleaned_data['workout_length']
            w_diff = form.cleaned_data['workout_difficulty']
            w_info = form.cleaned_data['workout_info']
            w = WorkoutRoutines(workout_title=w_title, workout_type=w_type,
            workout_length=w_length, workout_difficulty=w_diff, workout_info=w_info)
            if(WorkoutRoutines.objects.filter(workout_title=w_title).count()==0):
                w.save()
            print("new workout: ",w_title)
            form = NewWorkoutForm()
            print()
            return redirect('/workoutroutines/'+w_type+'/'+w_diff+'/')
#def process(request):

#    if request.POST.get('workout_type') is not None:
#        workouts_list = Workouts.objects.all()
#        workout_type = request.POST.get("workout_type")
#        workout_difficulty = request.POST.get("workout_difficulty")
#        workout_info = request.POST.get("workout_info")
#        workout = Workouts(workout_type=workout_type, workout_difficulty=workout_difficulty, workout_info=workout_info)
#        workout.save()

def choices(request):
    form= StartForm()
    #TODO moved render
    #return render(request, 'feed_app/form.html', {'form':form})

    # Used for choices page, redirect user to workout page, depending on workout type and difficulty
    if request.method=='POST':
        form=StartForm(request.POST)
        if form.is_valid():
            ex_diff=form.cleaned_data['ex_diff']
            ex_type= form.cleaned_data['ex_type']
            #print(ex_diff, ex_type)
            
            return redirect("/workoutroutines/"+ex_type+"/"+ex_diff+"/")
            #TODO delete
            
            #return redirect('workouts/')
    #TODO delete
    else:
        form=StartForm()
    return render(request, 'form.html', {'form':form})