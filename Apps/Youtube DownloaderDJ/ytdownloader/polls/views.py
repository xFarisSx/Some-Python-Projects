from re import template
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from pytube import YouTube, Playlist
import time
from django.template import loader

# Create your views here.
def index(request):
    url = request.GET.get('url')
    if url:
        
        yt = YouTube(url)
		
        video = {
				"info": {
					"title": yt.title,
					"author": yt.author,
					"thumbnail": yt.thumbnail_url,
					"description": yt.description,
					"length": time.strftime("%H:%M:%S", time.gmtime(yt.length)),
					"views": yt.views,
					"publish_date": yt.publish_date
				},
				"sources": []
			}
        videos = yt.streams.filter(progressive=True)
        for v in videos:
            video['sources'].append({
				"url": v.url,
				"size": f"{v.filesize//1048576} MB",
				"quality": v.resolution
			})
		
        template = loader.get_template('index.html')
        return JsonResponse(video)
    