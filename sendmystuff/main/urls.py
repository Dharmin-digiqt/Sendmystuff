from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^master/$', views.master, name='master'),
    url(r'^driver/$', views.driver, name='driver'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),
    url(r'^service/$', views.service, name='service'),
    url(r'^form/$', views.forms, name='form1'),
    url(r'^form2/$', views.forms2, name='form2'),

]
