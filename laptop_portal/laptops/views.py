from .models import Laptop
from django.shortcuts import render, redirect, get_object_or_404
from .forms import LaptopForm

def laptop_list(request):
    laptops = Laptop.objects.all()
    return render(request, 'laptops/laptop_list.html', {'laptops': laptops})

def laptop_list(request):
    laptops = Laptop.objects.all()
    return render(request, 'laptops/laptop_list.html', {'laptops': laptops})

def laptop_add(request):
    if request.method == 'POST':
        form = LaptopForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('laptop_list')  
    else:
        form = LaptopForm()
    return render(request, 'laptops/add_laptop.html', {'form': form})
