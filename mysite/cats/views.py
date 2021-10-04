from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Cat, Breed
# Create your views here.
class CatList(LoginRequiredMixin, ListView):
    model = Cat
    def get_context_data(self, **kwargs):
        BreedNum = Breed.objects.all().count()
        context = super().get_context_data(**kwargs)
        context['BreedNum']=BreedNum
        return context

class BreedList(LoginRequiredMixin, ListView):
    model = Breed

class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class BreedCreate(LoginRequiredMixin, CreateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class BreedUpdate(LoginRequiredMixin, UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

class BreedDelete(LoginRequiredMixin, DeleteView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy('cats:all')

