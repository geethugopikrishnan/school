from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"Invalid credentials")
            return redirect('signin')
    return render(request,'signin.html')


def logout(request):
    auth.logout(request)
    return render(request,'index.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already exist")
                return redirect('register')
            # if User.objects.filter(email=email).exists():
            #     messages.info(request,"Email ID already exist")
            #     return redirect('register')
            user = User.objects.create_user(username=username,password=password)
            user.save()
            print("user created")
            return redirect('signin')
        else:
            messages.info(request,"password not matching")
            return redirect('signup')
            return redirect('/')
    return render(request, 'signup.html')


