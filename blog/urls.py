from django.urls import path
from . import views
from .views import HomeView
from django.conf.urls import url

urlpatterns =[
  # url(r'^$', views.post_list, name='post_list'),
  # url(r'^post/?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
  path('', views.post_list, name= 'post_list'),
  path('post/<int:pk>/', views.post_detail, name = 'post_inhoud'),
  path('post/nieuw/', views.post_nieuw, name='post_nieuw'),
  
  # path('home', HomeView.as_view(),name="home"),
  # path('', views.post_list),
]
