from django.urls import path, include
from . import views

urlpatterns = [
    path('view/<int:id>', views.index, name='index'),
    path("", views.home, name="home"),
    path("create/", views.create, name="create"),
    path('view/', views.view, name="view"), 
    path('view/<int:item>/note', views.note, name="note"), 
]
