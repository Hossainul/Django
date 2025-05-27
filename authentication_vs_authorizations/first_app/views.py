from django.shortcuts import render,redirect
from .forms import registerForm,customUpdateform,customSetPasswordForm,userChangeData
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash

# Create your views here.

def signup_form(req):
    if not req.user.is_authenticated:
        if req.method == 'POST':
            form = registerForm(req.POST)
            if form.is_valid():
              user = form.save(commit=False)

              user.username = f"@{form.cleaned_data['first_name'].lower().replace(' ', '')}"
              user.save()
              messages.success(req,'Account created successfully !!')
              return redirect("home")
        else:
           form = registerForm()
        
        return render(req,'signup_form.html', {'form' : form})
    else:
        return redirect('profile')

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request = request, data = request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username = name, password = userpass)

                if user is not None:
                    login(request,user) 
                    return redirect('profile')
        else:
            form = AuthenticationForm()
        return render(request,'login_form.html', {'form' : form})
    else:
        return redirect('profile')


def profile(req):
    if req.user.is_authenticated:
      return render(req,'profile.html', {'user' : req.user})
    else:
        return redirect('login_form')
    
def Logout(req):
    logout(req)
    return redirect('login_form')

def passChange(req):
    if req.method == 'POST':
        form = customUpdateform(user = req.user, data = req.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(req, user = req.user)
            return redirect('profile')
    else :
        form = customUpdateform(user = req.user)
    
    return render(req,'passwordChange.html', {'form' : form})


def withoutOld(req):
    if req.method == 'POST':
        form = customSetPasswordForm(user = req.user, data = req.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(req, user = req.user)
            return redirect('profile')
    else :
        form = customSetPasswordForm(user = req.user)
    
    return render(req,'passwordChange.html', {'form' : form})

def updateEdit(req):
    if req.method == 'POST':
        form = userChangeData(req.POST, instance = req.user)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    else :
        form = userChangeData(instance = req.user)
        
    return render(req,'update_info.html', {'form' : form})