from django.urls import path
from myftsapp import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("register/", views.regist, name="regist"),
    path("login/", views.log, name="log"),
    path("survey/", views.mysurvey, name="mysurvey"),
    path('logout/',views.mylogout,name='mylogout'),
]