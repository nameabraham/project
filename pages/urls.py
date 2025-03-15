from django.urls import path
from . import views

urlpatterns = [
    path('register/' , views.register , name='register' ),
    path('' , views.home , name='home' ),
    path('logins/' , views.logins , name='logins' ),
    path('about/' , views.about , name='about'),
    path('footer/' , views.footer , name='footer'),
    path('join/' , views.join , name='join'),

]
