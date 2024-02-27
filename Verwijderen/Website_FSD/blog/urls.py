from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_inhoud'),
    path('post/nieuw/',views.post_nieuw,name='post_nieuw'),

    # toegevoegd ivm praktijkopdracht, delete knop toevoegen: views, post_inhoud en urls.py
    path('delete/<post_id>',views.delete_post,name='delete')
]