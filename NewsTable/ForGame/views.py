import requests
from django.views.generic import ListView, DeleteView, CreateView, UpdateView, DetailView
from .models import Post, Category, Comment, User
from .filters import PostFilter
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


# Create your views here.


class PostList(ListView):
    model = Post
    ordering = '-date'
    template_name = 'flatpages/post.html'
    context_object_name = 'post'
    paginate_by = 10


class CategoryList(ListView):
    model = Category
    template_name = 'flatpages/categorylist.html'
    context_object_name = 'category'


class PostDetail(DetailView):
    model = Post
    template_name = 'flatpages/postdetail.html'
    context_object_name = 'post'

    def post(self, request, **kwargs):
        post = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('postdetail', pk=post.pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context


@login_required
def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.add(user)

    message = "Подписка на категорию прошла успешно!"
    return render(request, 'flatpages/subscribe.html', {'category': category, 'message': message})


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


class ConfirmUser(UpdateView):
    model = User
    context_object_name = 'confirm_user'

    def post(self, request, *args, **kwargs):
        if 'code' in request.POST:
            user = User.objects.filter(code=request.POST['code'])
            if user.exists():
                user.update(is_active=True)
                user.update(code=None)
            else:
                return render(self.request, 'sign/invalid_code.html')
        return redirect('account_login')
