from django.contrib import admin

from .models import vegitables, customer
# Register your models here.



class CustomerBooking(admin.ModelAdmin):
    list_display = ('name','quantity','cust','address','phone')

class VegitableDetails(admin.ModelAdmin):
    list_display = ('name','price')

admin.site.register(customer,CustomerBooking)
admin.site.register(vegitables,VegitableDetails)