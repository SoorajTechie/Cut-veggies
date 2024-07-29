from django.shortcuts import render ,redirect ,get_object_or_404
from django.http import HttpResponse
from .forms import CustomerForm
from .models import customer ,vegitables
# Create your views here.

def home(request):
    return render(request, 'home.html')


def veg(request):

    if request.method == 'POST':
        form = CustomerForm(request.POST)
      
        if form.is_valid():
            order=form.save()
        
            #return redirect('order_success')
        return render(request, 'success.html',{'order':order})
    else:
        form = CustomerForm()  
    return render(request, 'veg.html',{'form':form})

def contact(request):
    return render(request, 'contact.html')

def dish(request):
    return render(request, 'dish.html')

def items(request):
    dict = {
        'veg': vegitables.objects.all()
    }
    return render(request, 'items.html',dict)


def about(request):
    return render(request, 'about.html')