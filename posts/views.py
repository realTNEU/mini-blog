from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post

@login_required
def create_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        
        if title and content:
            Post.objects.create(
                title=title,
                content=content,
                image=image,
                author=request.user
            )
            messages.success(request, 'Post created successfully!')
            return redirect('posts:list_posts')
        else:
            messages.error(request, 'Please provide both title and content.')
    
    return render(request, 'posts/create_post.html')

def list_posts(request):
    posts = Post.objects.all()
    return render(request, 'posts/list_posts.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'posts/post_detail.html', {'post': post})
