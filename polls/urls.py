from django.urls import path
from . import views

# urls here are sent to urls.py in main project folder
urlpatterns = [
    path('', views.index, name='index')
]
