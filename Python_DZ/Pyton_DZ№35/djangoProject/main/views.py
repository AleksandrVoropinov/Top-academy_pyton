from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, RecipeForm, CommentForm
from .models import Recipe, Comment, FavoriteRecipe, SavedRecipe


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'main/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'main/profile.html', context)


@login_required
def create_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.save()
            messages.success(request, f'Recipe created!')
            return redirect('recipe-detail', recipe.id)
    else:
        form = RecipeForm()

    context = {
        'form': form
    }

    return render(request, 'main/create_recipe.html', context)


@login_required
def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    comments = Comment.objects.filter(recipe=recipe)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.recipe = recipe
            comment.save()
            messages.success(request, f'Comment added!')
            return redirect('recipe-detail', recipe_id)
    else:
        form = CommentForm()

    context = {
        'recipe': recipe,
        'comments': comments,
        'form': form
    }

    return render(request, 'main/recipe_detail.html', context)


@login_required
def search_recipes(request):
    query = request.GET.get('q')

    if query:
        recipes = Recipe.objects.filter(title__icontains=query)
    else:
        recipes = Recipe.objects.all()

    context = {
        'recipes': recipes
    }

    return render(request, 'main/search_recipes.html', context)


@login_required
def add_to_favorites(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    favorite_recipe = FavoriteRecipe(user=request.user, recipe=recipe)
    favorite_recipe.save()
    messages.success(request, f'Recipe added to favorites!')
    return redirect('recipe-detail', recipe_id)


@login_required
def save_recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    saved_recipe = SavedRecipe(user=request.user, recipe=recipe)
    saved_recipe.save()
    messages.success(request, f'Recipe saved!')
    return redirect('recipe-detail', recipe_id)


def index(request):
    return None
