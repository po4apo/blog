from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


from post.models import Post


def main(requests):
    qs = Post.objects.all()
    #pogination = Paginator(qs, 1)
    return render(requests,'post/feed.html', {'objects_list':qs})

def test(requests):
    qs = Post.objects.all()
    return render(requests,'post/feed.html', {'objects_list':qs})

def show_post(requests, post_slug):
    qs = get_object_or_404(Post, slug = post_slug)
    return render(requests, 'post/post.html', {'objects_list': qs})