from django.conf.urls import patterns, url
from django.views.generic import RedirectView
from django.core.urlresolvers import reverse_lazy
from blog import views

urlpatterns = patterns('',
                       url(r'^$', views.posts, name='posts'),
                       url(r'^edit/$', views.edit, name='edit'),
                       url(r'^test/$', views.test, name='test'),
                       )
