from django.shortcuts import render
from django.http import HttpResponse

from .models import TestContent
# Create your views here.

def index(request):
	all_content = TestContent.objects
	return render(request, 'index.html', context)

def edit(request):
	all_content = TestContent.objects
	return render(request, 'edit.html', context)