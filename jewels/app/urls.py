from django.urls import path
from . import views
urlpatterns = [
path('',views.login),
path('logout',views.logout),
path('register',views.register),
path('userhome',views.userhome),
path('adminhome',views.adminhome),
]