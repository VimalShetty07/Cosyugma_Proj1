from django.urls import path
from accounts import views

urlpatterns = [
    path("", views.signin, name='signin'),
    path("signin", views.signin, name='signin'),
    path("signup", views.signup, name='signup'),
    path("otp/<uid>/", views.otp, name='otp'),
    path("index", views.index, name='index'),

]