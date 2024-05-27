# models.py
from django.db import models

class Ad(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)

# views.py
from django.shortcuts import render
from .models import Ad

def ad_list(request):
    ads = Ad.objects.all()
    return render(request, 'ad_list.html', {'ads': ads})

# forms.py
from django import forms
from .models import Ad

class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = ['title', 'description']

# urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('ads/', views.ad_list, name='ad_list'),
]

# registration/login functionality is not shown in this code snippet

# email sending functionality is not shown in this code snippet