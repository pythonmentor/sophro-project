from django.contrib.auth import forms
from django.shortcuts import render
from django.views import generic
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm, EditProfilForm

class UserRegisterView(generic.CreateView):
    form_class = SignUpForm
    template_name = 'registration/register.html'
    success_url=reverse_lazy('login')
    
class UserEditView(generic.UpdateView):
    form_class = EditProfilForm
    template_name = 'registration/profile.html'
    success_url=reverse_lazy('home')
    
    def get_object(self):
        return self.request.user
