from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from datetime import datetime
from post.models import Post, Coment
from post.forms import ComentForm


def main(request):
    qs = Post.objects.all()
    paginator = Paginator(qs, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    objects_list = {'posts': page_obj, }
    return render(request, 'post/feed.html', objects_list)


def show_post(requests, post_slug):
    post = get_object_or_404(Post,
                           slug=post_slug,
                             )
    com = Coment.objects.filter(post_id = post.id)

    if requests.method == 'POST':
        form = ComentForm(requests.POST)
        if form.is_valid():
            comment = form.save(commit = False)
            comment.post_id = post.id
            comment.postDate = datetime.now()
            comment.save()
    form = ComentForm()
    return render(requests, 'post/post.html', {'objects_list': post, 'form': form, 'com': com})


def show_projects(requests):
    return render(requests, 'post/feed.html')


