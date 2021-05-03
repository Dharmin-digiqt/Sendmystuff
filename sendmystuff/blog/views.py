from django.core.paginator import Paginator

from django.shortcuts import render
from .models import Blog, Site


# Create your views here.

def blog(request):

    # Paginator
    all_post = Blog.objects.all().order_by('id')
    paginator = Paginator(all_post, 3)
    page_no = request.GET.get('page')
    page_obj = paginator.get_page(page_no)

    d = {'page_obj': page_obj}
    return render(request, 'front/blog.html', d)


def blog_detail(request):
    return render(request, 'front/blog_detail.html')


def blog_master(request):
    return render(request, 'front/blog_master.html')


def about(request):
    site = Site.objects.get(pk=4)
    return render(request, 'front/about.html', {'bhagi': site})
