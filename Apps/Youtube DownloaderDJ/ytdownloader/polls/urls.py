from django.urls import path

from . import views

urlpatterns = [
    path('api/youtube/', views.index, name='index'),
]