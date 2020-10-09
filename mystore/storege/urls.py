from django.urls import path
from .views import View, PageHome, NewEntryView, EventsDetailview
 

 
urlpatterns = [
   # path('post/<int:pk>/', EventsDetailview.as_view(), name='post_detail'),
    path('', View.as_view(), name = 'home'),
    path('home/', PageHome.as_view(), name = 'index'),
    path('qwerty/', NewEntryView.as_view(), name = 'form'),
    path('i/<int:pk>/', EventsDetailview.as_view(), name='order_detail'),
    
]
