"""exercise URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from django.contrib import admin

from django.urls import path, re_path

from oauth_app import views as oauth_app_views

from oauth_app import views
from forum_app import views as forum_app_views
from workouts_app import views as workouts_app_views

urlpatterns = [
    #...

    path('', TemplateView.as_view(template_name="index.html")),
    #path('dashboard/', TemplateView.as_view(template_name="dashboard.html")),
    path('forums/', forum_app_views.forums_main, name="forums"),
    path('forums/submit-forum/', forum_app_views.submit_forum, name='submit_forum'),
    path('forums/<forum_id>/', forum_app_views.get_forum, name="forum_display"),
    path('forums/<forum_id>/submit-forum-post/', forum_app_views.submit_forum_post, name='submit_forum_post'),
    
    path('dashboard/', oauth_app_views.dashboard, name="dashboard"),
    path('accounts/', include('allauth.urls')),
    path('dashboard/profile/<username>/', oauth_app_views.get_user_profile, name='redirect-to-profile-page'),
    path('dashboard/profile/<username>/', oauth_app_views.get_user_profile, name="profile"),
    path('dashboard/profile/<username>/submit-profile/', oauth_app_views.submit_profile, name='submit_profile'),
    
   
    path('logout', LogoutView.as_view()),
    path('admin/', admin.site.urls),
   ######### path('profile/', TemplateView.as_view(template_name="profile.html")),
    path('friends/', TemplateView.as_view(template_name="friends.html")),
    path('archives/', TemplateView.as_view(template_name="archives.html")),
    path('progress/',TemplateView.as_view(template_name="progress.html")),
    path('challenges/',TemplateView.as_view(template_name="challenges.html")),
    #TODO take out namespace 
    #path('choices/', include('feed_app.urls', namespace='feed_app')),
    #path('choices/', include(('feed_app.urls','feed_app'), namespace= 'feed')),
    path('choices/',workouts_app_views.choices,name='workouts_main'),
    path('search/', include(('search.urls', 'search'), namespace= 'search')),
    
    #path('choices/workout', include('feed_app.urls')),
    #path('new-workout/', views.WorkoutsView.as_view(template_name="new_workout.html")), # this page
    #path('new-workout/workouts/list', oauth_app_views.workouts, name="workouts"),

    #path('new-workout/workouts/list', oauth_app_views.workouts, name="workouts"), # this url was used to test the workout submission form and populate one page of workouts
    #path('new-workout/workouts/cardio-easy', views.WorkoutsView.as_view(template_name="workouts/cardio_easy.html")),
    #path('new-workout/workouts/cardio-moderate', views.WorkoutsView.as_view(template_name="workouts/cardio_moderate.html")),
    #path('new-workout/workouts/cardio-difficult', views.WorkoutsView.as_view(template_name="workouts/cardio_difficult.html")),
    #path('new-workout/workouts/yoga-easy',views.WorkoutsView.as_view(template_name="workouts/yoga_easy.html")),
    #ath('new-workout/workouts/yoga-moderate',views.WorkoutsView.as_view(template_name="workouts/yoga_moderate.html")),
    #path('new-workout/workouts/yoga-difficult', views.WorkoutsView.as_view(template_name="workouts/yoga_difficult.html")),
    #path('new-workout/workouts/weightlifting-easy', views.WorkoutsView.as_view(template_name="workouts/weightlifting_easy.html")),
    #path('new-workout/workouts/weightlifting-moderate', views.WorkoutsView.as_view(template_name="workouts/weightlifting_moderate.html")),
    #path('new-workout/workouts/weightlifting-difficult',
     #    views.WorkoutsView.as_view(template_name="workouts/weightlifting_difficult.html")),


    path('workoutroutines/<workout_routine_id>/', workouts_app_views.get_workout_routine, name="workout_display"),
    path('workoutroutines/<type_id>/<diff_id>/', workouts_app_views.get_workout_list, name="workout_list_display"),
    path('add_points/', include('oauth_app.urls', 'add_points')),
    path('new-workout-routine/', workouts_app_views.WorkoutRoutinesView.as_view(template_name="new_workout_routine.html")),
    #path('new-workout-routine/process/', workouts_app_views.process, name="new_workouts_process"),
    

]