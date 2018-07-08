from django.contrib.auth import authenticate, logout
from django.contrib.auth.views import login
from django.http import HttpResponse
from django.shortcuts import render, redirect


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # print(request.user.is_authenticated)
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            redirect('posts:post-list')

        else:
            return redirect('members/login')

    else:
        return render(request, 'members/login.html')

def logout_view(request):
    # if request.method == 'POST':
        logout(request)
        return redirect('posts:post-list')