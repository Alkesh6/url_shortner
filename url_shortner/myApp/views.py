from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse("Hello World")


def homePage(request):
    context = {
        "submitted": False
    }
    # print(request.method)
    if request.method == 'POST':
        context["submitted"] = True
        data = request.POST
        long_url = data['longurl']
        customName = data['custom_name']
        print(long_url,"\n")
        print(customName)

        context["long_url"] = long_url
        context["custom_url"] = request.build_absolute_uri() + customName

    
    else:
        print("Not requesting any data")

    return render(request,'index.html',context)


def test(request):
    return render(request,'test.html')    