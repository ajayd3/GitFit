import requests 

from isodate import parse_duration

from django.conf import settings
from django.shortcuts import render

#followed a tutorial from 
# url: https://www.youtube.com/watch?v=lc2KvFbbfAQ
# title: Django Example App: YouTube Search With YouTube Data API
# author: Pretty Printed
# published: 07/27/2019 
# data accessed: 04/18/2021

def index(request):
    videos=[]
    if request.method == 'POST': 
        search_url= 'https://www.googleapis.com/youtube/v3/search'
        video_url= 'https://www.googleapis.com/youtube/v3/videos'
        search_params={
            'part': 'snippet', 
            'q': request.POST['search'],
            'key': settings.YOUTUBE_DATA_API_KEY,
            'maxResults': 9,
            'type': 'video'
        }
        video_ids=[]
        r=requests.get(search_url, params=search_params)
        results= r.json()['items']

        for result in results:
            video_ids.append(result['id']['videoId'])

        video_params= {
            'key': settings.YOUTUBE_DATA_API_KEY,
            'part': 'snippet,contentDetails',
            'id': ','.join(video_ids),
            'maxResults': 9
        }

        r= requests.get(video_url, params=video_params)

        results= r.json()['items']

        for result in results:
            video_data= {
                'title': result['snippet']['title'],
                'id': result['id'],
                'url': f'https://www.youtube.com/watch?v={ result["id"] }', 
                'duration': int(parse_duration(result['contentDetails']['duration']).total_seconds() // 60),
                'thumbnail': result['snippet']['thumbnails']['high']['url'],
            }

            videos.append(video_data)

    context={
        'videos': videos
    }
    return render(request, 'search/index.html', context)

def watch_video(request):
    video_id= request.POST.get('view_btn', None)
    context= {
        'video_id': video_id,
        'test_cont': "test_cont"
    }
    return render(request, 'search/watch_video.html', context)
