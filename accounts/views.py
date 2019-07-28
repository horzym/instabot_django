from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
# Create your views here.


def register(request):
     print('Register...')
     if request.method == 'POST':

         email = request.POST['email']
         password = request.POST['password']
         password2 = request.POST['password2']
         if request.POST['email'] == '':
            messages.error(request, 'Fill blank space!')
            return redirect('index')
         else:
            if password == password2:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is taken')
                    return redirect('index')
                else:
                    user = User.objects.create_user(
                    username=email, email=email, password=password)
                        #auth.login(request,user)
                        #messages.success(request,'Success login!')
                        #return redirect('index')
                    user.save()
                    messages.success(request, 'You are registered!')
                    return redirect('index')
            else:
                messages.error(request, 'Incorrect password!')
                return redirect('index')

def login(request):
    if request.method == 'POST':
        username=request.POST['email']
        password=request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,'Logged in!')
            return redirect('index')
        else:
            messages.error(request,'User not exist...')
            return redirect('index')
    