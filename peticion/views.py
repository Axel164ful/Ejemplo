from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
#-----------------------
from .models import Choice, Question
from django.template import loader
from django.urls import reverse
from django.views import generic

# Create your views here.
def pedir(request):
	return render(request, 'peticion/peticion1.html', {})
def pedir2(request):
	return render(request, 'peticion/peticion2.html', {})
def pedir3(request):
	return render(request, 'peticion/peticion3.html', {})