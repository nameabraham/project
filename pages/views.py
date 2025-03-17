from django.shortcuts import render , redirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate , login
from django.contrib import messages 
from .models import Jone


def home(request):
    return render(request , 'home.html')



def register(request):
    message = None 
    if request.method == "POST":
        name = request.POST["name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        if User.objects.filter(username=username).exists():
            message = "❌ اسم المستخدم مأخوذ بالفعل، يرجى اختيار اسم آخر."
            return render(request, "register.html", {"message": message})

        if User.objects.filter(email=email).exists():
            message = "❌ البريد الإلكتروني مستخدم بالفعل، يرجى استخدام بريد آخر."
            return render(request, "register.html", {"message": message})
        user = User.objects.create_user(username=username, email=email, password=password, first_name=name)
        user.save()
        message = "✅ تم التسجيل بنجاح! يمكنك الآن تسجيل الدخول."
        return render(request, "register.html", {"message": message})
    return render(request, "register.html", {"message": message})




def logins(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, "✅ تم تسجيل الدخول بنجاح!")
            return redirect("home")  
        else:
            messages.error(request, "❌ اسم المستخدم أو كلمة المرور غير صحيحة!")

    return render(request, 'logins.html')

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
