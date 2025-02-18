from django.urls import path
from . import views


urlpatterns = [
    path('profile/',views.profile,name='profile'),
    path('register/',views.register,name='register'),
    path('logout/',views.out,name='out'),
    path('login/',views.log,name='login'),
    path('update_password/',views.update_password,name='update_password'),
]
