from django.urls import path
from forum import views


urlpatterns = [
    path('', views.posts, name='posts'),
]
