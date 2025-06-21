from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm,UserChangeForm,PasswordChangeForm,SetPasswordForm
from .forms import registerForm,changePassword,updateInfo,user_addPost,addCommentForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib import messages
from .models import addPost,addComment

from django.views.generic import CreateView,UpdateView,DeleteView,DetailView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.
# def signUp(req):
#   if not req.user.is_authenticated:
#     if req.method == 'POST':
#         form = registerForm(req.POST)
#         if form.is_valid():
#            user =  form.save(commit=False)
#            first_part = form.cleaned_data['first_name']
#            last_part = form.cleaned_data['last_name']
#            password = form.cleaned_data['password1']

#            username = f"@{first_part.lower()}{last_part.lower()}"
#            print(username)
#            if User.objects.filter(username = username).exists():
#                form.add_error(None,"This user form is already exits !")
#            else :
#              user.username = username
#              user.save()
#              return redirect('Login')
            
#     else :
#         form = registerForm()
    
#     return render(req,'signup.html', {'form' : form })
#   else :
#       return redirect('Login')


from django.views.generic.edit import FormView
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from .forms import registerForm  # assuming you have this

class SignUpView(FormView):
    template_name = 'signup.html'
    form_class = registerForm
    success_url = reverse_lazy('Login')  # name of your login route

    def dispatch(self, request, *args, **kwargs):
        # Redirect if already logged in
        if request.user.is_authenticated:
            return redirect('Login')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        first = form.cleaned_data['first_name']
        last = form.cleaned_data['last_name']
        password = form.cleaned_data['password1']
        username = f"@{first.lower()}{last.lower()}"

        if User.objects.filter(username=username).exists():
            form.add_error(None, "This username already exists!")
            return self.form_invalid(form)

        user.username = username
        user.set_password(password)  # just in case
        user.save()

        messages.success(self.request, 'Account created successfully!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "There was an error creating your account.")
        return super().form_invalid(form)


# def Login(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request = request, data = request.POST)
#         if form.is_valid():
            
#             name = form.cleaned_data['username']
#             user_password = form.cleaned_data['password']
#             user = authenticate(username = name , password = user_password)

#             if user is not None:
#                 login(request,user)
#                 return redirect('profile')
    
#     else:
#         form = AuthenticationForm()

#     return render(request,'login.html', {'form' : form})

class userLogin(LoginView):
    template_name = 'login.html'
    # success_url = reverse_lazy('profile')

    def get_success_url(self):
        return reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'login successfully done !')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.success(self.request, 'login unsuccessfully done !')
        return super().form_invalid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'Login'
        return context
        
    

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

# def addPOST(req):
#     if req.method == 'POST':
#         form = user_addPost(req.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')
#     else:
#         form = user_addPost()
#     return render(req,'add_post.html', {'form' : form})

# add post class based view 
class appPostclassbasedview(CreateView):
    model = addPost
    form_class = user_addPost
    template_name = 'add_post.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.instance.author = self.request.user
        print("FILES:", self.request.FILES)
        print("Image file: ", self.request.FILES.get('image'))
        return super().form_valid(form)


def showPost(req):
    data = addPost.objects.all()
    return render(req,'post.html', {'data':data})

# def edit_post(req,id):
#     edit_form = addPost.objects.get(pk = id)
#     form = user_addPost(instance=edit_form)

#     if req.method == 'POST':
#         form = user_addPost(req.POST, instance = edit_form)
#         if form.is_valid():
#             form.save()
#             return redirect('profile')
#     else:
#       return render(req,'edit_post.html', {'form' : form})


class editPostView(UpdateView):
    model = addPost
    form_class = user_addPost
    template_name = 'edit_post.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('profile')
    
# def delete(req,id):
#     form = addPost.objects.get(pk = id)
#     form.delete()
#     return redirect('profile')

class deletePost(DeleteView):
    model = addPost
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')
    pk_url_kwarg = 'id'



class detailsView(DetailView):
    model = addPost
    template_name = 'details.html'
    pk_url_kwarg = 'id'
    context_object_name = 'author'

    # when you used class base view then you've to tell django what's you going to create
    def post(self, request, *args, **kwargs):
        comments_form = addCommentForm(data = self.request.POST)
        post = self.get_object()

        if comments_form.is_valid():
            new_comment = comments_form.save(commit= False)
            new_comment.post = post
            new_comment.save()
        return self.get(request,*args, **kwargs)

   
    # for showing data in templates 
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        post = self.object
        comments = post.comments.all()
        comments_form = addCommentForm()
        context['comment'] = comments
        context['contact_form'] = comments_form
        return context
       