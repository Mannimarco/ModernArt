import logging

from django.db import models
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.utils.timezone import now
from django.views.generic import CreateView, ListView,  UpdateView

from comment.models import Comment
from .forms import SearchForm, NewPostForm, EditPostForm
from .models import Post

logger = logging.getLogger(__name__)


class PostListView(ListView):
    model = Post
    template_name = 'post/post_list.html'
    queryset = Post.objects.all()
    ordering = 'created_date'
    paginate_by = 4
    search_form = None

    def dispatch(self, request, *args, **kwargs):
        self.search_form = SearchForm(request.GET)
        return super(PostListView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        search_form = SearchForm(self.request.GET)
        if search_form.is_valid():
            print(search_form.cleaned_data)
            order = search_form.cleaned_data['order']
            search = search_form.cleaned_data['text']
        else:
            order = self.request.GET.get('order_by', '-created_date')       # wtf?
            search = ''
        # queryset = Post.objects.filter(Q(title__icontains=search) and
        #                                Q(pub_date__lt=now()) and
        #                                Q(is_deleted=False))
        if self.request.user.is_authenticated():
            queryset = Post.objects.all().published().search(search).shown_for(self.request.user).order_by(order)
        else:
            queryset = Post.objects.all().published().search(search).order_by(order)
        queryset = queryset.stat()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['search_form'] = self.search_form
        return context


class CreatePostView(CreateView):
    model = Post
    template_name = 'post/post_create.html'
    form_class = NewPostForm

    def get_success_url(self):
        return reverse('post:detail', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        form.instance.author = self.request.user
        logger.info('i am logging')
        return super(CreatePostView, self).form_valid(form)


class PostAndCommentsView(CreateView):
    model = Comment
    template_name = "post/post.html"
    fields = ('text', )
    post = None

    def dispatch(self, request, pk=None, *args, **kwargs):
        # qs = Post.objects.stat()
        # self.post = get_object_or_404(qs, pk=pk)
        self.post = Post.objects.all().prefetch_related('comments', 'comments__author').select_related('author').get(pk=pk)
        return super(PostAndCommentsView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PostAndCommentsView, self).get_context_data(**kwargs)
        context['post'] = self.post
        return context


class EditPostView(UpdateView):
    model = Post
    template_name = 'post/post_edit.html'
    form_class = EditPostForm

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

    def get_success_url(self):
        return reverse('post:detail', kwargs={'pk': self.object.id})


class EditPostDialogView(UpdateView):
    model = Post
    template_name = 'post/post_edit_dialog.html'
    form_class = EditPostForm

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)

    def get_success_url(self):
        return reverse('post:detail', kwargs={'pk': self.object.id})
    
    def form_valid(self, form):
        response = super(EditPostDialogView, self).form_valid(form)
        return HttpResponse('OK')
        # return HttpResponse({'status': 'OK'})

    # def form_invalid(self, form):
    #     return HttpResponse({'status': 'FAIL', 'errors': form.errors.as_json()})
