
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views.generic import ListView, DeleteView, DetailView, CreateView, UpdateView
from .models import Post
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

# Create your views here.


class Homepage(ListView):
    model = Post
    template_name = 'post/post.html'
    context_object_name = 'posts'
    ordering = ['-id']


class Details(DetailView):
    model = Post
    template_name = 'post/postdetails.html'


class CreatePost(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post/newpost.html'
    success_url = '/'

    def form_valid(self1, form):
        form.instance.author = self1.request.user
        return super().form_valid(form)


class Delete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'post/delete.html'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    success_url = '/'


class updatePost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post/newpost.html'

    def form_valid(self1, form):
        form.instance.author = self1.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    success_url = '/'
