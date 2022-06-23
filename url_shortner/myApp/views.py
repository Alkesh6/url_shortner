import http
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import url

# Create your views here.
def hello(request):
    return HttpResponse("Hello World")


def homePage(request):
    context = {
        "submitted": False,
        "error" : False,
    }
    # print(request.method)
    if request.method == 'POST':
        context["submitted"] = True
        data = request.POST
        long_url = data['longurl']
        customName = data['custom_name']
        print(long_url,"\n")
        print(customName)

        try:
        #CREATE
            obj = url(long_url = long_url,short_url = customName)
            obj.save()

        #READ
            date = obj.date_field
            clicks = obj.clicks

            context["long_url"] = long_url
            context["custom_url"] = request.build_absolute_uri() + customName
            context["date"] = date
            context["clicks"] = clicks

        except:
            context["error"] = True

    
    else:
        print("Not requesting any data")

    return render(request,'index.html',context)


def redirect_url(request,short_url):
    row = url.objects.filter(short_url = short_url)

    if len(row) == 0:
        return HttpResponse("No such short url exist...")

    obj = row[0]
    long_url = obj.long_url

    obj.clicks = obj.clicks + 1
    obj.save()

    # print(long_url)
    return redirect(long_url)


def test(request):
    return render(request,'test.html')


def all_analytics(request):
    rows = url.objects.all()
    context = {
        'rows': rows
    }
    return render(request,'all-analytics.html',context)

