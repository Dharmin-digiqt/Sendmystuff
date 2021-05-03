from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.src_dst, name='home'),
    # url(r'^home/$', views.src_dst, name='home'),
    url(r'^src_dest/$', views.src_dst, name='home'),
    # url(r'^vehicles/$', views.vehicle, name='vehicle_form'),
    # url(r'^material/$', views.material, name='material_form'),
    # url(r'^user_login/$', views.user_login, name='login_form'),

    url(r'^form_one/$', views.form_one, name="form_one"),
    url(r'^form_two/$', views.form_test, name="form_two"),
]
