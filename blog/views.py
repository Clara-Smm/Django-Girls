from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

from .models import Post


def post_list(request):
    post_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    return render (request,"blog/post_list.html", {"lista":post_list})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

# Create your views here.
