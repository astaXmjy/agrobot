from django.urls import path
from . import views

urlpatterns = [
    # path('home/',views.Home,name='home'),
    path("weather/", views.weatherInfo, name="weather"),
    path("contact/", views.contactus, name="contact"),
    path('success/',views.success,name='success')
]
