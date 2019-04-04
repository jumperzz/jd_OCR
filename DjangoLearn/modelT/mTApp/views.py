from DjangoLearn.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def demo1(request):
    context = {"name":"Jumper"}
    context["age"] = 36
    context["arr"] = ["aa","bb","cc"]

    context["stu"] = {"name":"Tom","sex":"m","age":26}
    print(context["stu"]["name"])

    context['htmlinfo'] = "<h2>a</h2>"

    return render(request,"demo1.html",context=context)

def demo2(request):
    return render(request,"demo2.html")