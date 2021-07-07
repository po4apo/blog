import pathlib

import django.urls
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse


from post.models import Post, Image



def main(requests):
    qs = Post.objects.all()
    print(requests.path)
    objects_list = {'posts': qs,
                    }
    return render(requests,'post/feed.html', objects_list)


def show_post(requests, post_slug):
    qs = get_object_or_404(Post, slug = post_slug)
    return render(requests, 'post/post.html', {'objects_list': qs})

def show_projects(requests):
    return render(requests,'post/feed.html')

def show_about(requests):
    objects_list = {}
    # pogination = Paginator(qs, 1)
    return render(requests, 'post/feed.html', objects_list)