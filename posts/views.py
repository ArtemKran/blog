from django.shortcuts import redirect
from .models import Post, Comment
from .form import WritePostForm, EditPostForm, CommentForm
from django.views.generic.list import ListView
from datetime import datetime
from django.views.generic.edit import FormView, UpdateView
from django.core.urlresolvers import reverse

__author__ = 'Artem Kraynev'


class PostListView(ListView):
    """
    Главная страница с постами
    """
    template_name = 'posts.html'
    paginate_by = 5

    def get_queryset(self):
        return Post.objects.all().order_by('-id')

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        return context


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
        context['comments'] = Comment.objects.filter(
            post_id=self.kwargs['post_id']
        ).order_by('path')
        context['read_post'] = Post.objects.get(id=self.kwargs['post_id'])
        context['form'] = CommentForm()
        return context


def send_comment(request):
    """
    Обработка формы комментариев
    """
    form = CommentForm(request.POST)
    if request.POST:
        if form.is_valid():
            temp_form = form.save(commit=False)
            parent = form['parent'].value()
            if parent == '':
                temp_form.path = 0
                temp_form.save()
            else:
                node = Comment.objects.get(id=parent)
                temp_form.depth = node.depth + 1
                temp_form.path = node.path
                temp_form.save()
                temp_form.path = temp_form.id
            temp_form.save()
    return redirect(
        reverse('comment_post', kwargs={'post_id': form.data['post']})
    )


class PostWriteView(FormView):
    """
    Страница написания статьи
    """
    template_name = 'write_edit_post.html'
    form_class = WritePostForm
    success_url = '/'
    write = True

    def form_valid(self, form):
        form.save()
        return super(PostWriteView, self).form_valid(form)


class PostEditView(UpdateView):
    """
    Страница редактирования статьи
    """
    template_name = 'write_edit_post.html'
    form_class = EditPostForm
    write = False
    pk_url_kwarg = 'post_id'
    query_pk_and_slug = 'post_id'
    model = Post

    def get(self, request, *args, **kwargs):
        self.initial['post'] = Post.objects.get(id=self.kwargs['post_id'])
        return super(PostEditView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.success_url = reverse(
            'comment_post',
            kwargs={'post_id': self.kwargs['post_id']}
        )
        return super(PostEditView, self).post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PostEditView, self).get_context_data(**kwargs)
        now = datetime.now()
        context['date'] = datetime.strftime(now, "%d.%m.%Y")
        context['post'] = Post.objects.get(id=self.kwargs['post_id'])
        return context


