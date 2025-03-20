from django.urls import path
from . import views

app_name = 'forum'

urlpatterns = [
    path('', views.index, name='index'),
    path('choose_username/', views.choose_username, name='choose_username'),
    path('submit/', views.submit_post, name='submit_post'),
]
