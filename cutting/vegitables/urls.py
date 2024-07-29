from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('vegetables/',views.veg, name='veg'),
    path('dishes/',views.dish, name='dish'),
    path('contact/',views.contact,name='contact'),
    path('available-veg/',views.items,name='avail'),
    path('about_us/',views.about,name='about')
]
