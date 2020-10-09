from django.shortcuts import render, redirect, get_object_or_404
from .models import Storege, Order, Merchandise
from django.views.generic import CreateView, ListView, DetailView
from .forms import EntryForm
from django.urls import reverse_lazy
# Create your views here.

class View(ListView):
    model = Storege
    template_name = 'Layout/base.html'
   

class PageHome(ListView):
    model = Order
    template_name = 'home.html'

    #def stor(request):
        #last_hist = storege.models.orderr_connect_stor.objects.all()
        #context = {
        #'last_hist': last_hist,
       #  }
       # return render(request, 'home.html', context)
    #e = Order.objects.select_related('storege_admin').get(self.request.user)
    #def get_queryset(self):
        #return super().get_queryset().filter(storege_admin = Order.objects.select_related('storege_admin').get(self.request.user))
        #Order.objects.select_related('storege_admin').get(self.request.user)
    #def get_queryset(self):
       # return super().get_queryset().filter(orderr_connect_stor=self.request.user)
    #queryset = Order.objects.filter(storege_admin = user.name) #фільтр по юзеру


class EventsDetailview(DetailView):
    model = Order
    template_name = 'content.html'
    #def get_object(self):
       # return get_object_or_404(self.model, storege_admin = self.request.user)


class NewEntryView(CreateView):
    form_class=EntryForm
    template_name='formorder.html'
    def get_success_url(self):
        return  reverse_lazy ('form')      
