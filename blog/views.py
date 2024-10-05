from typing import Any
from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from .models import Post,Comment,Category
from .forms import PostForm,CommentForm,UpdatePostForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


def list_post_view(request):
    if request.method == "POST":
        query = request.POST['query_search']
        if query:
            posts = Post.objects.filter(title__icontains=query)
    else:
        posts = Post.objects.all()

    return render(request,'post/listPosts.html',{'posts':posts})

def category_view(request,pk):
    posts = Post.objects.filter(category_id=pk)

    return render(request,'post/listPosts.html',{'posts':posts})

class CreatePostView(LoginRequiredMixin,CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post/createPost.html'
    success_url = '/'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    

class UpdatePostView(LoginRequiredMixin,UpdateView):
    model = Post
    form_class = UpdatePostForm
    template_name = 'post/updatePost.html'
    success_url = '/'
    
class DeletePostView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = '/'

@login_required
def handle_post_view(request,pk):
    post = Post.objects.get(pk=pk)
    comments = Comment.objects.filter(post=post)
    if request.method =="POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            Comment.objects.create(content=content,post=post,author=request.user)
            return redirect('view_post',pk=pk)

    else:
        form = CommentForm()

    return render(request,'post/viewPost.html',{'form':form,'post':post,"comments":comments})
