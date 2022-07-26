from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about_us', views.about_us, name='about'),
    path('create', views.create, name='create'),
    path('examples', views.examples, name='examples'),
]