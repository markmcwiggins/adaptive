from django.conf.urls import url, include

from . import views

urlpatterns = [
    url('^', include('django.contrib.auth.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^[0-9]?[0-9][0-9].html', views.hand, name='hand'),
    url(r'^2d.html', views.twod, name='twod'),
    url(r'^2clubs.html', views.twoclubs, name='twoclubs'),
    url(r'^1heart.html', views.oneheart, name='oneheart'),
    url(r'answer_proc', views.answer_proc, name='answer_proc'),
    url(r'^wrong/$', views.wrong, name='wrong'),
    url(r'^randpage/$', views.randpage, name='randpage'),
    url(r'^right/$', views.right, name='right'),
]

