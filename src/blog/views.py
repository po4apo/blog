from django.shortcuts import render


def show_about(requests):
    objects_list = {}
    return render(requests, 'about.html', objects_list)