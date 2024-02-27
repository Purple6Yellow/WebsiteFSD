from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Post
from django.views.generic import ListView, DetailView
from .forms import PostForm

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html',{'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post':post})

class HomeView(ListView):
    model = Post
    template_name = 'blog/home.html'

def Agenda (request):
    return render (request, 'blog/home.html', {'name': 'Violette'})

def post_nieuw(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save (commit = False) 
            post.author = request.user
            post.publish_date = timezone.now()
            post.save()
            return redirect ('blog/post_inhoud', pk=post.pk)
        else:
            form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})
   
