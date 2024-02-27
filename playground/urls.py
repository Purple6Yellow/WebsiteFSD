from django.urls import path
from . import views

urlpatterns = [
        path('hello1/', views.say_hallo1),
        path('hello2/', views.say_hallo2),
        path('Agenda.html/', views.Agenda),
        path('Blog.html/', views.Blog),
        ##
        path('',views.home_index),
        path('Overons.html/', views.Overons),
        path('Tarieven.html/', views.Tarieven),
        path('Contact.html/', views.Contact),
        path('Index.html/', views.home_index),
        path('BlogJava.html/',views.BlogJava),
        path('Blog5.html/',views.Blog5),
        path('Blogdetail.html/',views.Blogdetail),
        path('BlogInvullen.html/',views.BlogInvullen)
          ]
