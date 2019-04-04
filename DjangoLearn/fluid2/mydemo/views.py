from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator


from .models import Fluid

# Create your views here.
def myweb(request):
    return render(request,"myweb/users/index.html")

#===============搜索和分页========================
def stu(request):
    lists = Fluid.objects.all()
    context = {"list":lists}
    # print('列表中的数据是',context)
    return render(request,"myweb/users/stu.html",context)

def stupage(request,pIndex):
    lists = Fluid.objects.all()
    p = Paginator(lists,2)
    plist = p.page_range
    pCount = p.count

    # print(pCount/2)
    # print(type(pCount))
    # print("pIndex:"+pIndex)
    if int(pIndex) <= 0 :
        pIndex = int(pIndex) + 1
    elif int(pIndex) > int(pCount/2):
        pIndex = int(pCount/2)

    list2 = p.page(pIndex)
    context = {"list":list2,"plist":plist,"pIndex":int(pIndex)}
    return render(request,"myweb/users/stupage.html",context)

def stusearch(request):
    lists = Fluid.objects.get_queryset().order_by('id')

    name = request.GET.get("name","")
    # print("获取到的name是",name)
    if name != "":
        lists = lists.filter(name__contains=name)

    sex = request.GET.get("sex","")
    # print("获取到的sex是",sex)
    if sex != "":
        lists = lists.filter(sex=sex)

    context = {"list":lists}
    # print('列表中的数据是',context)
    return render(request,"myweb/users/stusearch.html",context)

def stuspages(request,pIndex):
    lists = Fluid.objects.filter()
    condition = []
    name = request.GET.get("name","")
    if name != "":
        lists = lists.filter(name__contains=name)
        condition.append("name="+name)

    sex = request.GET.get("sex","")
    if sex != "":
        lists = lists.filter(sex=sex)
        condition.append("sex="+sex)

    # print("condition",condition)
    p = Paginator(lists,2)
    pCount = p.count

    if int(pIndex) <= 0:
        pIndex = int(pIndex) + 1
    elif int(pIndex) > int(pCount / 2):
        pIndex = int(pCount / 2)

    list2 = p.page(pIndex)
    plist = p.page_range

    context = {"list":list2,"plist":plist,"pIndex":pIndex,"condition":condition}
    return render(request,"myweb/users/stuspages.html",context)

def ct(request):
    cname = request.COOKIES.get("classname","c1")
    print("canme:",cname)
    context = {"classname":cname}
    return render(request,"myweb/ct.html",context)

def setCt(request):
    response = HttpResponse("<script>window.location='/myweb/ct'</script>")
    cc = request.GET.get("cname","")
    print("cc:",cc)
    if cc != "":
        response.set_cookie("classname",cc,3600)
    return response

def se(request):
    num = request.session.get("num",0)
    num += 1
    request.session["num"] = num
    return HttpResponse("计数器的值:"+str(num))

#继承实例 自己编写的
def extends(request):
    lists = Fluid.objects.all()
    context = {"list":lists}
    return render(request,'myweb/extends/extends.html',context)
