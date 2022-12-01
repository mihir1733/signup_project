from django.contrib import admin
from django.urls import path
from signup import views

urlpatterns = [
    path('',views.signup_view,name='signup'),
    path('login',views.login_view,name='login'),
    path('next',views.next,name='next'),
]
