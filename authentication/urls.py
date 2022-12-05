from django.urls import path 
from authentication import views

urlpatterns = [
    path('', views.authredirect , name='authredirect'), 
    path('register/', views.register , name='register'), 
    path('signin/', views.signin , name='signin'), 
    path('signout/', views.signout , name='signout'), 
]