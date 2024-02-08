from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('create_recipe/', views.create_recipe, name='create_recipe'),
    path('profile/', views.profile, name='profile'),
    path('recipe_detail/', views.recipe_detail, name='recipe_detail'),
    path('register/', views.register, name='register'),
    path('search_recipes/', views.search_recipes, name='search_recipes'),
]
