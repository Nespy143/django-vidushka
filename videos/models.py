from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to="videosa/thumbnails")
    source = models.FileField(upload_to="videosa")

    def __str__(self):
        return f"{self.id} - {self.title}"