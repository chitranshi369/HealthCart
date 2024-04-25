from django.shortcuts import render,redirect
from django.views import View
from customer.forms import *
from django.http import HttpResponse

class CustomerSignup(View):
    def get(self,request):
        return render(request,'customer/signup.html')
    
    def post(self,request):
        data = request.POST
        myform = MyUserForm(data=data)
        if myform.is_valid():
            myform.save()
            # return redirect("log-in")
        else:
            return HttpResponse("error")

class CustomerLogin(View):
    
    def get(self,request):
        return render(request,'customer/login.html')


