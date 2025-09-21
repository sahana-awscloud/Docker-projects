from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('update/<str:pk>/', views.updateTask, name="update"),
    path('delete/<str:pk>/', views.deleteTask, name="delete"),
    path('toggle/<str:pk>/', views.toggleTask, name="toggle"),
]
