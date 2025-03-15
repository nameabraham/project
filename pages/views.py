from django.shortcuts import render , redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate , login
from django.contrib import messages 
from .models import Jone


def home(request):
    return render(request , 'home.html')


def register(request):
    if request.method == "POST":
        firstname = request.POST.get('firstname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            request.session['message'] = "اسم المستخدم موجود "
            return redirect('logins')
        
        if User.objects.filter(email=email).exists():
            request.session['message'] = " الايميل مسجل مسبقا"
            return redirect('loginns')
        
        myuser = User.objects.create_user( username=username , email=email , password=password)
        myuser.first_name = firstname
        myuser.save()
        request.session['messgae']='تم انشاء الحساب بنجاح'
        return redirect('logins')
    
    return render(request , 'register.html')



def logins(request):
     if request.method == "POST":
      username = request.POST.get('username')
      password = request.POST.get('password')
      user = authenticate( request , username=username , password=password)
      if user is not None:
          login(request , user)
          return redirect('home')
      else:
        #   request.session['message'] = " ليس لديك حساب "
          return redirect('register')
     return render(request , 'logins.html')


def about(request):
    return render(request , 'about.html')

def footer(request):
    return render(request , 'footer.html')

def join(request):
    if request.method == "POST":
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        phone = request.POST.get('phone', '').strip()
        skills = request.POST.get('skills', '').strip()
        experience = request.POST.get('experience', '').strip()
        message = request.POST.get('message', '').strip()

        Jone.objects.create(
            name=name,
            email=email,
            phone=phone if phone else None,    
            skills=skills,
            experience=experience
        )

        messages.success(request, "🎉 تم تقديم الطلب بنجاح!")
        return redirect('join')  # إعادة تحميل الصفحة بعد الإرسال

    return render(request, 'join.html')


def buy(request):
    return render(request , 'buy.html')

def support(request):
    return render(request , 'support.html')
