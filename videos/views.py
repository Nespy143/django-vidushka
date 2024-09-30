from django.shortcuts import render, redirect
from .models import Video, Comment
from .forms import CommentForm

def video_page(request, video_id):
    video = Video.objects.get(pk=video_id)
    comments = video.comments.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(text=request.POST['text'], author=request.user, video=video)
            comment.video = video
            comment.save()
            return render(request, 'video/video.html', {'video': video})
    else:
        form = CommentForm()
    context = {'video': video, 'comments': comments, 'form': form}
    return render(request, 'video/video.html', context)
