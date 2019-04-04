from DjangoLearn.shortcuts import render
from DjangoLearn.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello World!")
