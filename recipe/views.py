from django.shortcuts import render
from .models import Recipe, Category
from django.db.models import Count

def main(request):
    latest_recipes = Recipe.objects.order_by('-created_at')[:5] 
    return render(request, 'main.html', {'recipes': latest_recipes})
