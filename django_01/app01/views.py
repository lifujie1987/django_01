from django.shortcuts import render
from django.shortcuts import HttpResponse
from app01 import models
# Create your views here.

def news(request,n1):


    return HttpResponse(n1)

def db_handle(request):





    # for item in user_info_obj:
    #     print(item.username)
    # return HttpResponse("ok")
    if request.method=='POST':
        # print(request.POST)
        models.UserInfo.objects.create(username=request.POST['username'],
                                       password=request.POST['password'],
                                       age=request.POST['age'])
    user_info_obj=models.UserInfo.objects.all()
    return render(request,'t1.html',{'li':user_info_obj})