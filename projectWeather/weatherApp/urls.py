from django.urls import path

from weatherApp import views

app_name = 'weatherApp'

urlpatterns = [
    path('', views.index, name='home'),
    # path('ip_home', views.home, name='ip_home'),

]
