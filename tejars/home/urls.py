from django.urls import path

from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('blogdetails',views.blogdetails,name='blogdetails'),


]