from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from . import forms
from . import models

# Create your views here.

class carAdd(LoginRequiredMixin,CreateView):
    template_name = "add_car.html"
    form_class = forms.carAddingform
    success_url = reverse_lazy("profile")

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class carViews(ListView):
    template_name = "home.html"
    model = models.addCar
    context_object_name = "cars"

    def get_queryset(self):
        query_set = models.addCar.objects.all()

        query_title = self.request.GET.get('search','')

        if query_title:
            query_set = query_set.filter(car_model__icontains = query_title) # car_model filter by this name 
        return query_set
    
    
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       context["search_term"] = self.request.GET.get("search", "")
       return context

class carEdit(LoginRequiredMixin,UpdateView):
    template_name = "car_edit.html"
    form_class = forms.carAddingform
    model = models.addCar
    success_url = reverse_lazy("all_cars")

class carDelete(LoginRequiredMixin,DeleteView):
    model = models.addCar
    template_name = "delete_car.html"
    success_url = reverse_lazy("all_cars")