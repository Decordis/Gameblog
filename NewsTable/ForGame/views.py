from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from .models import Post, Category, Comment
from .filters import PostFilter
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


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


class PostCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'ForGame.add_post'
    form_class = PostForm
    model = Post
    template_name = 'flatpages/postcreate.html'


class PostUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = 'ForGame.change_post'
    form_class = PostForm
    model = Post
    template_name = 'flatpages/postupdate.html'


class PostDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'ForGame.delete_post'
    model = Post
    template_name = 'flatpages/postdelete.html'
    success_url = reverse_lazy('post')


class AddComments(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = 'ForGame.add_comment'
    form_class = CommentForm
    model = Comment
    template_name = 'flatpages/postdetail.html'