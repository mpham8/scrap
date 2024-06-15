from . import views
from django.urls import path


urlpatterns = [
  path('agenda/', views.agenda, name = 'agenda'),
  path('', views.home, name = 'home'),
  path('login/', views.loginPage, name = 'login'),
  path('logout/', views.logoutPage, name = 'logout'),
  path('register/', views.registerUser, name = 'register')
]