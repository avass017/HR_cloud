from django.urls import path

from Hr_cloud_app import views

urlpatterns = [
 path('',views.index,name='index'),
 path('Login',views.Login,name='Login'),
]
