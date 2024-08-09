from django.contrib import admin
from django.urls import path, include
from core.views import landing, signup
from core import views
from django.urls import path
from core.views import landing, user_login  # Import the views

from core.views import landing, signup, user_login 
from core.views import home_view 
   
   


urlpatterns = [
    path('', landing, name='landing'),
    path('app/', include('core.urls')), 
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.login_view, name='logout'),  # This will link the logout URL to the login view.
    path('', views.index, name='index'),
    path('routes/', views.routes, name='routes'),
    path('login/', user_login, name='user_login'),
    path('signup/', signup, name='signup'),
    path('login/', user_login, name='login'),
    
    path('', views.index, name='index'),
    path('routes/', views.routes, name='routes'),

    path('home/', home_view, name='home'),

]
