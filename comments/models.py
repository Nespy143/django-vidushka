from django.db import models
from django.contrib.auth.models import User

class Video(models.Model):
    # Add some fields for the video, e.g. title, description, etc.
    title = models.CharField('Название видео', max_length=255)
    description = models.TextField('Описание видео')

class Comment(models.Model):
    text = models.TextField('Текст комментария')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
