from django.http.response import HttpResponse
from django.shortcuts import render ,redirect
from django.contrib.auth.forms import UserCreationForm ,AuthenticationForm # for login
from django.contrib.auth import login ,logout


def signupView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user) # to login too afters signing up
            return HttpResponse('you have been signed up!!')


    form = UserCreationForm()
    return render(request,'accounts/signUp.html',{'form':form})

def loginView(request):
    if request.method == 'POST':
        form=AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('/polls/blog')


    form = AuthenticationForm()
    return render(request,'accounts/login.html',{'form':form})

def logoutView(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/accounts/login')