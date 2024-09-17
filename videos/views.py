from lib2to3.fixes.fix_input import context

from django.http import HttpResponse, HttpRequest
from django.shortcuts import render

def video_page(request: HttpRequest ) -> HttpResponse:
    video = models.Video.objects.get(pk=1)
    context = {'video': video}
    return render(request, 'video/video.html', context)
