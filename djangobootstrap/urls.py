from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about_us'),
    path('post/', views.post, name='posts'),
    path('contact/', views.contact, name='contact_us'),
]
