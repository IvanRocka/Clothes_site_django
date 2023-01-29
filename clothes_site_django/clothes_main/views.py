import datetime

from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return HttpResponse("Страница приложения clothes_main.")

def categories(request, cat_name):
    if(request.GET):
        print(request.GET)
    return HttpResponse(f"<h1> Статьи по категориям одежды</h1><p>{cat_name}</p>")

def archive(request, year):
    if int(year) > datetime.date.today().year:
        #raise Http404()
        return redirect('home', permanent=False)
    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1> Страница не найдена </h1>')