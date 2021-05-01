from django.shortcuts import render, get_object_or_404
from .models import Blog


def all_blogs(request):
    """
    Blog function
    :return:
    """
    blog_lst = Blog.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {'blogs': blog_lst})


def detail(request, blog_id):
    """
    Return blog detail
    :param request: request by the user
    :param blog_id: ID of the called blog
    :return:
    """
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': blog})
