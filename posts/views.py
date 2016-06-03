from django.shortcuts import render_to_response, redirect
from django.template.context_processors import csrf
from .models import Post, Comment
from .form import WritePostForm, EditPostForm, CommentForm
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic.list import ListView
from datetime import datetime


__author__ = 'Artem Kraynev'


def posts(request):
    """
    Главная страница с постами
    """
    html = 'posts.html'
    # Можно было использовать и order_by()
    # и get_object_or_404(), но думаю для тестового
    # не принципиально - исключение или 400
    posts_all = [i for i in reversed(Post.objects.all())]
    paginator = Paginator(posts_all, 4)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    post_dict = {
        'posts': posts,
    }
    post_dict.update(csrf(request))
    return render_to_response(html, post_dict)


class CommentsListView(ListView):
    """
    Страница с отдельной статьей и комментариями
    """
    template_name = 'read_post.html'
    model = Comment

    def get_queryset(self):
        return Comment.objects.filter(post_id=self.kwargs['post_id'])

    def get_context_data(self, **kwargs):
        context = super(CommentsListView, self).get_context_data(**kwargs)
        context['read_post'] = Post.objects.get(id=self.kwargs['post_id'])
        context['comments_form'] = CommentForm()
        return context


def read_post_and_write_comment(request):
    """
    Обработка формы комментариев
    """
    if request.POST:
        url = '/' + request.POST['post'] + '/'
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            parent_id = comment_form.data['parent_id']
            if parent_id != '':
                comment_form.instance.parent = Comment.objects.get(id=parent_id)
                comment_form.save()
            else:
                comment_form.save()
            return redirect(url)


def write_post(request):
    """
    Страница написания статьи
    """
    html = 'write_edit_post.html'
    write_post_dict = {
        'write': True,
        'form': WritePostForm(),
    }
    write_post_dict.update(csrf(request))
    if request.POST:
        write_post_form = WritePostForm(request.POST)
        if write_post_form.is_valid():
            write_post_form.save()
            return redirect('/')
        else:
            write_post_dict['form'] = write_post_form
    return render_to_response(html, write_post_dict)


def edit_post(request, post_id):
    """
    Страница редактирования статьи
    """
    html = 'write_edit_post.html'
    now = datetime.now()
    edit_post_dict = {
        'post': Post.objects.get(id=post_id),
        'form': EditPostForm(),
        'date': datetime.strftime(now, "%d.%m.%Y"),
    }
    edit_post_dict.update(csrf(request))
    if request.POST:
        edit_post_form_query = Post.objects.get(id=post_id)
        edit_post_form = EditPostForm(
            request.POST, instance=edit_post_form_query
        )
        if edit_post_form.is_valid():
            edit_post_form.save()
            return redirect('/')
        else:
            edit_post_dict['form'] = edit_post_form
    return render_to_response(html, edit_post_dict)
