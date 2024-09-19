from django.urls import path, include
from . import views

urlpatterns = [
    path('<int:video_id>', views.video_page)
]