from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from post.models import Post


def main(request):
    qs = Post.objects.all()
    paginator = Paginator(qs, 1)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    objects_list = {'posts': page_obj, }
    return render(request, 'post/feed.html', objects_list)


def show_post(requests, post_slug):
    qs = get_object_or_404(Post, slug=post_slug)
    return render(requests, 'post/post.html', {'objects_list': qs})


def show_projects(requests):
    return render(requests, 'post/feed.html')


def show_about(requests):
    objects_list = {}
    return render(requests, 'post/feed.html', objects_list)
