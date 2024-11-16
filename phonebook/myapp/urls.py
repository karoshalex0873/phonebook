from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.show, name='show'),
    path('index/', views.display, name='home'),
    path('delete/<int:id>/', views.delete, name='delete'),
     path('edit/<int:user_id>/', views.edit_user, name='edit_user'),
]