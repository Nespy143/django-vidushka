from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from videos import models


def video_page(request: HttpRequest, video_id: int ) -> HttpResponse:
    video = models.Video.objects.get(pk=video_id)
    context = {'video': video}
    return render(request, 'video/video.html', context)
