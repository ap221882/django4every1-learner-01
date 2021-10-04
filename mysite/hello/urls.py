from django.urls import path

app_name = 'hello'

from . import views

urlpatterns = [
    path('', views.myview, name='hello')
    ]