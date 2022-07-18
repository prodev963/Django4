from django.urls import include
from django.urls import path
from my1app import views

#Template tagging

app_name = 'my1app'

urlpatterns = [   
    path('registration/', views.registration, name='registration'),
    path('user_login/', views.user_login, name='user_login'),
]
