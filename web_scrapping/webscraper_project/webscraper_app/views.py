import lib2to3.pgen2.tokenize

from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import requests
from bs4 import BeautifulSoup
from .models import Links


# Create your views here.



def home(request):
    if request.method=='POST':
        elink=request.POST.get('page')
        urls=requests.get(elink)
        beatifulsoup=BeautifulSoup(urls.text,'html.parser')
        for link in beatifulsoup.find_all('a'):
            li_adress=link.get('href')
            li_strname=link.string
            Links.objects.create(adress=li_adress,strname=li_strname)
        return HttpResponseRedirect('/')
    else:
        data_values=Links.objects.all()
    return render(request,'home.html',{'data_values':data_values})


def clear(request):
    if request.method=='POST':
        web=Links.objects.all()
        web.delete()
        return redirect('/')
    return render(request,'delete.html')