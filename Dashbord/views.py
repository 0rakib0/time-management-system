from django.shortcuts import render, HttpResponse

# Create your views here.

def Dashbord (request):
    return render(request, 'Dashbord/dashbord.html')
