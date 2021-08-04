from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from aboutme.models import Info
from django.views.generic import ListView


def show_about(requests):
    qs = Info.objects.all()
    return render(requests, 'aboutme/about.html', {'objects_list': qs})


class HomePageView(ListView):
    model = Info
    template_name = 'home.html'