from django.urls import path
from . import views
urlpatterns = [
path('',views.login),
path('logout',views.logout),
path('register',views.register),
path('shopregister',views.shopregister),
path('userhome',views.userhome),
path('adminhome',views.adminhome),
path('shophome',views.shophome),
path('addpro',views.addpro),
path('viewpro',views.viewpro),
path('edit/<int:id>',views.edit),
path('delete/<int:id>',views.delete),


]