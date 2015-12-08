from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^user/', include('registration.backends.simple.urls')),
    url(r'^user/', include('django.contrib.auth.urls')),
                       url(r'^review/create/$', ReviewCreateView.as_view(), name='review_create'),
                      url(r'review/$', ReviewListView.as_view(), name='review_list'),
                       url(r'^review/(?P<pk>\d+)/$', ReviewDetailView.as_view(), name='review_detail'),
                       url(r'^review/update/(?P<pk>\d+)/$', ReviewUpdateView.as_view(), name='review_update'),
       url(r'^review/delete/(?P<pk>\d+)/$', ReviewDeleteView.as_view(), name='review_delete'),
                       url(r'^review/(?P<pk>\d+)/comment/create/$', CommentCreateView.as_view(), name='comment_create'),
                       url(r'^review/(?P<review_pk>\d+)/comment/update/(?P<comment_pk>\d+)/$', CommentUpdateView.as_view(), name='comment_update'),
                      url(r'^review/(?P<review_pk>\d+)/comment/delete/(?P<comment_pk>\d+)/$', CommentDeleteView.as_view(), name='comment_delete'),
                      )
