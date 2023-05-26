from django.shortcuts import render
from .models import Arcticle, Category

# Create your views here.

def index(request):
    return render(request, 'index.html', {})

def arcticles_list(request):
    arcticles = Arcticle.objects.all()
    category = Category.objects.all()

    return render(request, 'arcticle/view.html', {'arcticles':arcticles, 'category': category })