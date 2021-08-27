from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import REDIRECT_FIELD_NAME, authenticate,login
from .models import Profile
from django.http import HttpResponse
from django.template import loader
import pdfkit
import io
# Create your views here.
# Create your views here.
def index1(request):
    return render(request,'page.html')
# def login(request):
#     return render(request,'login.html')
def login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
        return redirect('home')
    return render(request,'login.html')

def accept(request):
    if request.method=="POST":
        name=request.POST.get("name","")
        phone=request.POST.get("phone","")

        email=request.POST.get("email","")
        school=request.POST.get("school","")
        degree=request.POST.get("degree","")
        university=request.POST.get("university","")
        skills=request.POST.get("skills","")
        about_you=request.POST.get("about_you","")
        profile=Profile(name=name,phone=phone,email=email,school=school,degree=degree,university=university,skills=skills,about_you=about_you)
        profile.save()

    
    return render(request, "accept.html")

def resume(request,id):
    user_profile=Profile.objects.get(pk=id)
    template=loader.get_template("resume.html")
    html=template.render({'user_profile':user_profile})
    option={
        'page-size':'Letter',
        'encoding':'UTF-8'
    }
    pdf=pdfkit.from_string(html,False,option)
    response=HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition']='attachment'
    filename="resume.pdf"
    return response

def list(request):
    profile=Profile.objects.all()
    return render(request,"list.html",{'profile':profile})
def notes(request):
    return render(request,'to_do_main.html')
def quize(request):
    return render(request,'choice.html')
def python(request):
    return render(request,'python.html')
def java(request):
    return render(request,'java.html')
def newpage(request):
    return render(request,"page1.html")
def chquize(request):
    return render(request,'choice1.html')
def adnotes(request):
    return render(request,'addnotes.html')








    
    