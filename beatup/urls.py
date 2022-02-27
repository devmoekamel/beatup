from unicodedata import name
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home , name='home'),
    path('community/', views.postpage , name='community'),
    path('addpost/', views.addpost , name='addpost'),
    path('editpost/<str:pk>/',views.edit_post,name='editpost'),
    path('user_profile/<str:pk>/',views.user_profile,name='userprofile'),
    path('deletepost/<str:pk>/',views.delete_post,name='deletepost'),
    path('login/', views.loginpage , name='loginpage'),
    path('logout/', views.logoutpage , name='logoutpage')
]
