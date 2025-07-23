from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib import messages
from Profile.models import Profile

from . import form
# Create your views here.

class signUp(FormView):
    template_name = 'register.html'
    form_class = form.registerUser
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit = False)
        user.save()
        
        Profile.objects.create(
            user = user,
            is_seller = form.cleaned_data['seller']
        )
        messages.success(self.request, 'Account created successfully !')
        return super().form_valid(form)
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)
    

class loginUser(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy("profile")


# class logoutUser(LogoutView):
#     template_name = 'logout.html'
#     success_url = reverse_lazy('login')