from django.shortcuts import render
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from .models import Post, Category
from .filters import PostFilter
from .forms import PostForm


# Create your views here.


class PostList(ListView):
    model = Post
    ordering = '-date'
    template_name = 'flatpages/post.html'
    context_object_name = 'post'
    paginate_by = 10

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     self.filterset = NewsFilter(self.request.GET, queryset=queryset)
    #     return self.filterset.qs
    #
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['filterset'] = self.filterset
    #     return context


class PostDetail(DetailView):
    model = Post
    template_name = 'flatpages/postdetail.html'
    context_object_name = 'post'


class PostSearch(ListView):
    model = Post
    template_name = 'flatpages/postsearch.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'flatpages/postcreate.html'
