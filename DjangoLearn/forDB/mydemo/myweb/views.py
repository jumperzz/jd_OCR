from DjangoLearn.shortcuts import render
from DjangoLearn.http import HttpResponse

from .models import Users

# Create your views here.
def myweb(request):
    lists = [{'id':10,'name':'one'},
             {'id': 11, 'name': 'two'},
             {'id': 12, 'name': 'three'},
             {'id': 13, 'name': 'four'},
             ]
    context = {"name":"jumper","list":lists}
    return render(request,"myweb/index.html",context)

    # return HttpResponse('Hello World!')

def add(request):
    return HttpResponse('add...')

def dels(request,uid):
    return HttpResponse('del...'+request.path+':'+str(uid))

def userIndex(request):
    # ob = Users.objects.get(id=1)
    # print(ob.name)
    # res = Users.objects.all()
    # res = Users.objects.filter(name='jack')
    # print(res)
    lists = Users.objects.all()
    context = {"list":lists}
    return render(request,"myweb/users/index.html",context)

    # return HttpResponse('user')

def usersdel(request,uid):
    ob = Users.objects.get(id=uid)
    ob.delete()
    return HttpResponse("del ok")