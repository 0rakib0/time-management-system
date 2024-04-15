from django.urls import path
from . import views

app_name = 'portfolio'

urlpatterns = [
    path('add-skills/', views.add_skills, name='add_skill')
]