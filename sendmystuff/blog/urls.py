from django.conf.urls import url
from .import views

urlpatterns = [

    url(r'^blog/$', views.blog, name='blog'),
    url(r'^blog_master/$', views.blog_master, name='blog_master'),
    url(r'^blog/detail/$', views.blog_detail, name='blog_detail'),
    url(r'^about/$', views.about, name='about'),
]
