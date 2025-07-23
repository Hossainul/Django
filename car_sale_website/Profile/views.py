from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView,ListView
from django.core.exceptions import ValidationError
from Car import models
from . import form,models


from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import logout
from django.views import View


# Create your views here.

@login_required
def userProfile(request):
    return render(request, 'profile.html')


class passwordChange(LoginRequiredMixin,PasswordChangeView):
    template_name = "passwordchange.html"

    def get_success_url(self):
        return reverse_lazy("profile")
    
    def form_valid(self,form):
        messages.success(self.request,'password changed successfully !')
        return super().form_valid(form)

@login_required
def logout_confirm(request):
    return render(request, 'logout.html')

@login_required
def logout_user(req):
    logout(req)
    return redirect("login")

class editProfile(LoginRequiredMixin,UpdateView):
    template_name = "edit_profile.html"
    form_class = form.editProfileForm
    success_url = reverse_lazy("profile")


    def get_object(self, queryset=None):
        return self.request.user.profile
    
    def get_context_data(self, **kwargs):
       context =  super().get_context_data(**kwargs)

       if self.request.POST:
           context['user_form'] = form.userForm(self.request.POST, instance=self.request.user)
       else:
           context['user_form'] = form.userForm(instance=self.request.user)

       return context
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        profile_form = self.get_form()
        user_form = form.userForm(self.request.POST, instance=self.request.user)

        if profile_form.is_valid() and user_form.is_valid():
            user_form.save()
            profile_form.save()

            messages.success(self.request,'profile updated successfully !')
            return redirect("profile")
        
        return self.form_invalid(profile_form)


class allCars(LoginRequiredMixin, ListView):
    template_name = "car_views.html"
    form_class = models.addCar
    context_object_name = "cars"

    def get_queryset(self):
        return models.addCar.objects.filter(user = self.request.user)



class buyCar(LoginRequiredMixin,View):
    def post(self,request, car_id):
        car = get_object_or_404(models.addCar, id = car_id)
        quantity = int(request.POST.get('quantity', 1))

        if quantity < 1 or quantity > car.car_quantity:
            return ValidationError("your entered wrong number !")
        
        total_price = quantity * car.car_price

        models.order.objects.create(
            user = request.user,
            car = car,
            quantity = quantity,
            total_price = total_price
        )

        car.car_quantity -= quantity
        car.save()

        return redirect("user_history")


class UserHistoryView(LoginRequiredMixin, ListView):
    model = models.order
    template_name = "user_history.html"
    context_object_name = "orders"

    def get_queryset(self):
        return models.order.objects.filter(user=self.request.user).select_related('car').order_by('-ordered_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orders = context['orders']
        context['total_spent'] = sum(order.total_price for order in orders)
        context['total_cars'] = sum(order.quantity for order in orders)
        return context