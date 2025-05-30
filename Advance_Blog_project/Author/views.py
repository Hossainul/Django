from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserChangeForm,PasswordChangeForm,SetPasswordForm
from .forms import registerForm,changePassword,updateInfo,user_addPost
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
from .models import addPost

# Create your views here.
def signUp(req):
  if not req.user.is_authenticated:
    if req.method == 'POST':
        form = registerForm(req.POST)
        if form.is_valid():
           user =  form.save(commit=False)
           first_part = form.cleaned_data['first_name']
           last_part = form.cleaned_data['last_name']
           password = form.cleaned_data['password1']

           username = f"@{first_part.lower()}{last_part.lower()}"
           print(username)
           if User.objects.filter(username = username).exists():
               form.add_error(None,"This user form is already exits !")
           else :
             user.username = username
             user.save()
             return redirect('Login')
            
    else :
        form = registerForm()
    
    return render(req,'signup.html', {'form' : form })
  else :
      return redirect('Login')

def Login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request = request, data = request.POST)
        if form.is_valid():
            
            name = form.cleaned_data['username']
            user_password = form.cleaned_data['password']
            user = authenticate(username = name , password = user_password)

            if user is not None:
                login(request,user)
                return redirect('profile')
    
    else:
        form = AuthenticationForm()

    return render(request,'login.html', {'form' : form})

def Logout(req):
    logout(req)
    return redirect('homepage')

def profile(req):
    return render(req,'profile.html')

def changePass(req):
    if req.method == 'POST':
        form = changePassword(user = req.user, data = req.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(req,user = req.user)
            messages.success(req,"Password changed successfully !!")
            return redirect('profile')
            
    else:
        form = changePassword(user = req.user)
    
    return render(req,'updatepass.html', {'form' : form})


def changePasswithoutold(req):
    if req.method == 'POST':
        form = SetPasswordForm(user = req.user, data = req.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(req,user = req.user)
            messages.success(req,"Password changed successfully !!")
            return redirect('profile')
            
    else:
        form = SetPasswordForm(user = req.user)
    
    return render(req,'updatepass.html', {'form' : form})

def updateData(req):
    if req.method == 'POST':
        form = updateInfo(req.POST, instance = req.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        
    else:
        form = updateInfo(instance = req.user)

    return render(req,'update_info.html', {'form' : form})

def addPOST(req):
    if req.method == 'POST':
        form = user_addPost(req.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = user_addPost()
    return render(req,'add_post.html', {'form' : form})

def showPost(req):
    data = addPost.objects.all()
    return render(req,'post.html', {'data':data})

def edit_post(req,id):
    edit_form = addPost.objects.get(pk = id)
    form = user_addPost(instance=edit_form)

    if req.method == 'POST':
        form = user_addPost(req.POST, instance = edit_form)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
      return render(req,'edit_post.html', {'form' : form})
    
def delete(req,id):
    form = addPost.objects.get(pk = id)
    form.delete()
    return redirect('profile')