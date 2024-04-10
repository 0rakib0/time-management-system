from django.shortcuts import render,  redirect
from django.contrib.auth import login, authenticate
# Create your views here.

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Dashbord:dashbord')
        else:
            print('User not Found')
    return render(request, 'Accounts/Login.html')