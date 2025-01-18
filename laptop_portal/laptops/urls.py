from django.urls import path
from . import views

urlpatterns = [
    path('', views.laptop_list, name='laptop_list'),  # Home page
    path('add/', views.laptop_add, name='laptop_add'),  # Add laptop page
]
