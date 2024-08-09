# core/urls.py
from django.contrib import admin
from django.urls import path
from . import views
from .views import landing, signup, user_login
from .views import login_view, home_view 





urlpatterns = [
    path('', views.landing, name='landing'),
    path('login/', views.login_view, name='login'),
    path('signup/', signup, name='signup'),
    
   
    path('logout/', views.logout_view, name='logout'),
    path('routes/', views.routes, name='routes'),

    
    path('signup/', views.sign_up, name='signup'),
    path('login/', login_view, name='login'),
    path('index/', views.index, name='index'),
    path('home/', home_view, name='home'), 
    



    
     

]








