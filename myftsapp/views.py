from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import  logout
from django.contrib import messages



def home(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')
  

# Create your views for registration with email sending
def regist(request):
    if request.method == "POST":
        form = hotel_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful.")
            return redirect("/login")
          
        else:      
             messages.error(request, "Unsuccessful registration")
             return render(request=request, template_name="register.html", context={"register_form": form})
    form = hotel_form()
    return render(request=request, template_name="register.html", context={"register_form": form})

def log(request):
    
    if request.method=="POST":
        form= login_form(request.POST) # always when login use request.post 
        username = request.POST["username"]
        password = request.POST["password"]
            
        obj = SignUp.objects.filter(username=username,password=password)  # to authenticate from model class i-e signup
            
           
        if (obj.count() > 0):    
            request.session['uid'] = request.POST['username']  # to login the page and session is also create
            messages.success(request,"login successfull")
            return redirect("/survey")

        else:
             messages.error(request," invalid username or password")
        return render(request=request, template_name="login.html", context={"login_form": form}) 

    else:
        form= login_form()
    return render(request=request, template_name="login.html", context={"login_form": form}) 

def mysurvey(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        age=request.POST['age']
        phone=request.POST['phone']
        comment =request.POST['comment']
        contact=survey(name=name, email=email, age=age, phone=phone, comment=comment)
        contact.save()
        messages.success(request,"Form submitted successfully")
        return redirect("/")
    else:    
        return render(request, 'survey.html')   

def mylogout(request):
    if request.session.has_key('uid'):
      del request.session['uid'] 
      logout(request)  #to delete session and logout the page with import logout from django.contrib.auth
      messages.success(request,"logout successfull")
      return redirect("/")
    else:
        return redirect('/login')       