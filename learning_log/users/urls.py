""" define urls of users """

from django.conf.urls import url
from django.contrib.auth.views import login

from . import views

urlpatterns = [
    # login
    url(r'^login/$',login,{'template_name':'users/login.html'},name='login'),

    # logout
    url(r'^logout/$', views.logout_view, name='logout'),

    # logup
    url(r'^register/$',views.register,name='register'),
]
