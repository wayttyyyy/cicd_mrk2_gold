from django.test import TestCase
from django.urls import reverse
from .models import Category, Recipe


class RecipeViewsTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Desserts")
        Recipe.objects.create(
            title="Cake", description="Yummy", 
            instructions="Bake", ingredients="Flour", 
            category=self.category
        )

    def test_main_view(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main.html')
        self.assertIn('recipes', response.context)
        