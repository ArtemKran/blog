from django.conf.urls import url
from . import views

__author__ = 'Artem Kraynev'

urlpatterns = [
    url(r'^$', views.posts),
    url(r'^(?P<post_id>\d+)/$', views.CommentsListView.as_view()),
    url(r'^set_comment/$', views.read_post_and_write_comment),
    url(r'^write/$', views.write_post),
    url(r'^edit/(?P<post_id>\d+)/$', views.edit_post),
]

