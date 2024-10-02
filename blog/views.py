from django.shortcuts import render,redirect
from django.urls import reverse
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from .models import Post,Comment
from .forms import PostForm,CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# Create your views here.

class ListPostView(LoginRequiredMixin,ListView):
    model = Post
    template_name = 'post/listPosts.html'
    context_object_name = 'posts'


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
    fields = ['title','content']
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
            Comment.objects.create(content=content,post=post)
            return redirect('view_post',pk=pk)

    else:
        form = CommentForm()

    return render(request,'post/viewPost.html',{'form':form,'post':post,"comments":comments})
