from django.db import models
from django.db.models import fields
from django.http import request
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


from .models import Category, Post
from .forms import EditForm, PostForm

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']
    
    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(HomeView, self).get_context_data(*args, **kwargs)
        context["cat_menu"] = cat_menu
        return context
    
def CategorylistView(request):
    cat_menu_list = Category.objects.all()
    return render(request, 'categories_list.html', {'cat_menu_list':cat_menu_list})
        
def CategoryView(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request, 'categories.html', {'cats':cats.title().replace('-', ' '), 'category_posts':category_posts})
    
class ArticleDetailsView(DetailView):
    model = Post
    template_name='article_details.html'
    
class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name='add_post.html'
    
class AddCategoryView(CreateView):
    model = Category
    # form_class = PostForm
    template_name='add_category.html'
    fields = '__all__'
    
class UpdatepostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    
class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    
