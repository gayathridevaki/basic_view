from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from app.forms import *


# Create your views here.
class httpresponse(View):
    def get(self,request):
        return HttpResponse('this is the string from class based view')
    
class htmlpage(View):
    def get(self,request):
        return render(request,'htmlpage.html')


class insert_school(View):
    def get(self,request):
        SFO=schoolform()
        d={'SFO':SFO}
        return render(request,'insert_school.html',d)
    def post(self,request):
        SFDO=schoolform(request.POST)
        if SFDO.is_valid():
            SFDO.save()
        return HttpResponse('inserted successfully')