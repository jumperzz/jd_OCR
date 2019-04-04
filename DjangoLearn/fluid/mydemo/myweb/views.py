from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator


from .models import Fluid

# Create your views here.
def myweb(request):
    return render(request,"myweb/users/index.html")

#===============搜索和分页========================
def stu(requset):
    lists = Fluid.objects.all()
    context = {"list":lists}
    print('列表中的数据是',context)
    return render(requset,"myweb/users/stu.html",context)

def stupage(request,pIndex):
    lists = Fluid.objects.all()
    p = Paginator(lists,2)

    list2 = p.page(pIndex)
    context = {"list":list2}

def stusearch(request):
    pass

def stuspages(request):
    pass