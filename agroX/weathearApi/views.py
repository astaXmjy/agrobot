from django.shortcuts import render
from django.http import HttpResponseRedirect
import requests
from django.shortcuts import HttpResponse
from .form import ContactUs
# Create your views here.


def weatherInfo(request):
    if "city" in request.GET:
        city = request.GET["city"]
        url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=06a4a737b6d27218037c44e6687c4d82"
        city_weather = requests.get(url.format(city)).json()
        weather = {
            "city": city,
            "temperature": round((city_weather["main"]["temp"] - 32) / 1.8),
            "description": city_weather["weather"][0]["description"],
            "icon": city_weather["weather"][0]["icon"],
        }
        return render(request, "weather.html", {"weather": weather})

    return render(request, "weather.html")


def contactus(request):
    if request.method=='POST':
        form=ContactUs(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect('/weather/')

    else:
        form=ContactUs()

    return render(request,'contact.html',{'form':form})


def success(request):
    return HttpResponse('success')
