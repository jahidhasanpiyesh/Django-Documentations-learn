from django.shortcuts import render
from django.http import HttpResponse

# Create your views here and functions.
def index(request):
    return HttpResponse("Hello My Friends")

def home(request):
    return HttpResponse("Hello My Developer Team")