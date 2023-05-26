from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.arcticles_list, name='arcticles_list'),
]
