from Django.shortcuts import render
from Django.http import HttpResponse
from .models import Users

# Create your views here.
def userIndex(request):
    ob = Users.objects.all()
    context = {"list":ob}
    return render(request,"index.html",context)

def userDel(request,id):
    print(id)
    return HttpResponse('okokok')

