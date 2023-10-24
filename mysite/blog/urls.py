#Dit bestand zelf toegevoegd, om bestand in mysite/urls.py overzichtelijk te houden. 

from django.urls import path
from .import views

urlpatterns = [
    path('', views.post_list, name = 'post_list'),
]