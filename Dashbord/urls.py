from django.urls import path
from . import views

app_name = 'Dashbord'

urlpatterns = [
    path('dashbord/', views.Dashbord, name='dashbord')
]