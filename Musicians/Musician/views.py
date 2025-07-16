from django.urls import path
from django.shortcuts import redirect,render
from .forms import registerUser,passwordChange,passwordChangeWithout,ProfileForm,addAlbumForm,UserForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Profile,addALBUM

from django.contrib.auth.views import PasswordChangeView,LoginView,LogoutView
from django.views.generic import CreateView,ListView
from django.urls import reverse_lazy
from django.views.generic import FormView,UpdateView,DetailView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin 

# function based views
# def signUp(req):
#     if req.user is not authenticate:    
#         if req.method == 'POST':
#             form = registerUser(req.POST)
#             if form.is_valid():
#                 form.save()
#                 messages.success(req,'account created successfully !!')
#                 return redirect("login")
#         else:
#             form = registerUser()
    
#         return render(req,'register.html', {'form' : form})
#     else:
#         return redirect('login')
    

# class based views

class signUp(FormView):
    template_name = 'register.html'
    form_class = registerUser
    success_url = reverse_lazy('login')

    def form_valid(self,form):
        print("FORM IS VALID")
        print(form.cleaned_data)
        user = form.save(commit = False)
        user.save()

        # create profile with musician status
        # This code help me to create a profile with 'is_musician' field that's why i can access this field in my templates like this "user.profile.is_musician".

        Profile.objects.create(
            user = user,
            is_musician = form.cleaned_data['is_musician']
        )
       
        messages.success(self.request, 'Account created successfully !')
        return super().form_valid(form)
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)
    

@login_required
def profile(req):
    return render(req,'profile.html')




# def loginUser(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request=request, data=request.POST)
#         if form.is_valid():
#             name = form.cleaned_data['username']
#             password = form.cleaned_data['password']
#             user = authenticate(username=name, password=password) 

#             if user is not None:
#                 print("yeas")
#                 login(request, user)
#                 print("no")
#                 return redirect('profile') 
#     else:
#         form = AuthenticationForm()
    
#     return render(request, 'login.html', {'form': form})

# class based views 
class CustomLoginView(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('profile')

#class based viwes for logout
# class LogoutConfirmView(View):
    
#     def get(self, request):
#         return render(request, 'logout_confirm.html')

# class LogoutView(View):
   
#     def post(self, request):
#         logout(request)
#         return redirect("login")

#function based logout
@login_required
def logout_confirm(request):
    return render(request, 'logout.html')

@login_required
def logOUT(request):
    logout(request)
    return redirect("login")

# def passwordChangeUser(req):
#     if req.method == 'POST':
#         form = passwordChange(user = req.user, data = req.POST)
#         if form.is_valid():
#             form.save()
#             update_session_auth_hash(req, req = req.user)
#             return redirect('profile')
#     else:
#         form = passwordChange(user = req.user)
    
#     return render(req,'changePassword.html', {'form' : form})


# def changepasswithout(req):
#     if req.method =='POST':
#         form = passwordChangeWithout(user = req.user, data = req.POST)
#         if form.is_valid():
#             form.save()
#             update_session_auth_hash(req, user = req.user)
#             return redirect('profile')
#     else:
#         form = passwordChangeWithout(user = req.user)
    
#     return render(req,'changePassword.html', {'form' : form})



# class based views for changing password with old one 
class mypasswordchange(PasswordChangeView):
    template_name = 'changePassword.html'
    
    def get_success_url(self):
        return reverse_lazy('profile')
    
    def form_valid(self,form):
        messages.success(self.request, 'Password changed successfully !!')
        return super().form_valid(form)
    


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'edit_profile.html'
    success_url = reverse_lazy('profile')
    
    #`get_object()` tells the view: "Here’s the specific `Profile` instance to update".
    #self.request.user.profile`: grabs the profile belonging to the currently logged-in user.

    def get_object(self, queryset=None):
        return self.request.user.profile
    
    # get_context_data() is how we pass extra data (like another form) to the template.
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if self.request.POST:
            context['user_form'] = UserForm(self.request.POST, instance=self.request.user)
        else:
            context['user_form'] = UserForm(instance=self.request.user)
        return context
    
    
    # This function runs when the user submits the form (clicks save).
    def post(self, request, *args, **kwargs):
        self.object = self.get_object() # This is required by Django’s `UpdateView` to know what object to update
        profile_form = self.get_form() # get_form() returns the submitted ProfileForm.
        user_form = UserForm(request.POST, instance=request.user) # Then we also build a UserForm with submitted data.

        if profile_form.is_valid() and user_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect(self.success_url)

        return self.form_invalid(profile_form)
    

    # you can also used get object to fetching profile data 
    # def get_object(self):
    #     return self.request.user.profile
    

    # def get_object(self, queryset=None):
    #     # Get or create profile for the current user
    #     profile, created = Profile.objects.get_or_create(user=self.request.user)
    #     return profile

    # def get_form_kwargs(self):
    #     kwargs = super().get_form_kwargs()
    #     kwargs['user'] = self.request.user  # Pass user to the form
    #     return kwargs
    
# add album

class addAlbum(LoginRequiredMixin,CreateView):
    template_name = 'add_album.html'
    model = addALBUM
    form_class = addAlbumForm
    
    def form_valid(self, form):
      form.instance.user = self.request.user
      return super().form_valid(form)
    
    def get_success_url(self):
        return reverse_lazy('profile')

class profileView(LoginRequiredMixin,ListView):
    model = addALBUM
    template_name = 'Album_View.html'
    context_object_name = 'albums'
    ordering = ['-Release_date']

    def get_queryset(self):
      queryset =  addALBUM.objects.filter(user=self.request.user)

      # get search filter parameter
      title_query = self.request.GET.get('search','')

      if title_query:
          queryset = queryset.filter(title__icontains = title_query)
      return queryset
    
    # it only stored your entered value and 'Hybrid Theory' in search box
    # def get_context_data(self, **kwargs):
    #     context =  super().get_context_data(**kwargs)
    #     context['search_term'] = self.request.GET.get('search','')
    #     return context
    

class allAlbumViews(ListView):
    model = addALBUM
    template_name = 'home.html'
    context_object_name = 'albums'
    ordering = ['-Release_date']
    

    def get_queryset(self):
        queryset = addALBUM.objects.all()

        query_title = self.request.GET.get('search','')

        if query_title:
            queryset = queryset.filter(title__icontains = query_title)
        return queryset

class deleteAlbum(LoginRequiredMixin,DeleteView):
    model = addALBUM
    template_name = "album_confirm_delete.html"
    success_url = reverse_lazy("show_album")


class editAlbum(LoginRequiredMixin,UpdateView):
    model = addALBUM
    form_class = addAlbumForm
    template_name = "edit_album.html"
    success_url = reverse_lazy("profile")
