from django.conf.urls import url
from . import views

__author__ = 'Artem Kraynev'

urlpatterns = [
    url(r'^$', views.PostListView.as_view(), name='post_list'),
    url(r'^(?P<post_id>\d+)/$', views.CommentsListView.as_view(), name='comment_post'),
    url(r'^send_comment/$', views.send_comment, name='send_comment'),
    url(r'^write/$', views.PostWriteView.as_view(), name='write_post'),
    url(r'^edit/(?P<post_id>\d+)/$', views.PostEditView.as_view(), name='edit_post'),
]

