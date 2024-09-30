from django.db import models
from django.contrib.auth.models import User

class Video(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="videosa/thumbnails")
    source = models.FileField(upload_to="videosa")

    def __str__(self):
        return f"{self.id} - {self.title}"

class Comment(models.Model):
    text = models.TextField('Текст комментария')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    def __str__(self):
        return self.text