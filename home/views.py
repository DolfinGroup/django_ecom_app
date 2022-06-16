from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login


#from register.models import Post

# Create your views here.
def index(request):
   # return HttpResponse("This is home page")

   context={
       'variable':"this is sent varible",
       "var2" : "Var 2 "
   }
   return render(request, 'index.html',context)

def login(request):

    if request.method == 'POST':
        loginuser = request.POST['loginusername']
        loginpass = request.POST['loginpassword']
        print(loginuser)
        print(loginpass)
        user  = authenticate(username = loginuser, password= loginpass)

        if user is not None:
            auth_login(request, user)
            messages.success(request, 'successfull Logged In....')
            return render(request,'index.html')
        else:
            messages.error(request, "Invalid Username and Password")
            return redirect('/login')
    else:
      return render(request,'login.html')

def about(request):
    #return HttpResponse("This is about page")
    return render(request, 'about.html')

def service(request):
   # return HttpResponse("This is service page")
   return render(request, 'service.html')

   
def contact(request):
    return render(request,'contact.html')


def help(request):
    return render(request,'help.html')

def register(request):

    if request.method == "POST":
       username = request.POST['fname']
       fname = request.POST['lname']
       email = request.POST['email']
       phno = request.POST['phno']
       pass1 = request.POST['pass1']
      # pass2 = request.POST['pass2']
       
       myuser= User.objects.create_user(username,email,pass1)
       myuser.fname = fname
       myuser.email = email
       myuser.phno = phno
       myuser.pass1 = pass1
       myuser.save()
       messages.success(request, "succesfull submited")
       return redirect('/login')
    else:
         return render(request,'register.html')

    #return render(request,'register.html')
   



        


