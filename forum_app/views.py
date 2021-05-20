from django.shortcuts import render, redirect
from .models import Forum, ForumPost
from django.utils import timezone
from django.contrib.auth.models import User
# Create your views here.
def forums_main(request):
    context = {"forums": Forum.objects.all()}
    return render(request, 'forums_main.html', context)

def submit_forum(request):
    if(request.method=="POST"):
        f = Forum(title=request.POST['title_field'], description=request.POST['description_field'], time_started=timezone.now())
        f.save()
    return redirect("/forums/")

def submit_forum_post(request, forum_id):
    f=Forum.objects.get(id=forum_id)
    if(request.method=="POST"):
        fp = ForumPost(text=request.POST['forum_text_field'], time_posted=timezone.now(), user=request.user, forum=f)
        fp.save()
    context = {"forum" : f, "forum_posts" : f.forumpost_set.all()}
    return render(request, 'forum.html', context)

def get_forum(request, forum_id):
    f=Forum.objects.get(id=forum_id)
    print(f.forumpost_set.all())
    context = {"forum" : f, "forum_posts" : f.forumpost_set.all()}
    return render(request, 'forum.html', context)