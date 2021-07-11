from django.contrib.auth import login
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='mainsite'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout_request, name = 'logout'),
    path('login/',views.login_request, name='login'),
]
