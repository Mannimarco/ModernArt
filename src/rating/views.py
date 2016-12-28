import json

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from django.shortcuts import get_object_or_404
from django.views import View

from post.models import Post
from rating.forms import VoteForm
from rating.models import Vote


class PostRatings(View):

    def get(self, request):
        posts = dict()
        ids = request.GET.get('ids', '')
        ids = ids.split()
        for post in Post.objects.filter(id__in=ids):
            posts[post.id] = post.get_rating()
        return HttpResponse(json.dumps(posts))


class PostRatingValueView(View):

    post = None

    def dispatch(self, request, pk=None, *args, **kwargs):
        self.post = get_object_or_404(Post, pk=pk)
        return super(PostRatingValueView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        return HttpResponse(self.post.get_rating())


@login_required
def vote_up(request, pk):
    return do_vote(request, pk, 1)


@login_required
def vote_down(request, pk):
    return do_vote(request, pk, -1)


def do_vote(request, pk, value):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        vote = Vote.objects.get_or_create(post=post, author=request.user, defaults={'value': 0})
        vote.value += value

        if Vote.objects.filter(post=post, author=request.user).count() == 1:
            vote = Vote.objects.get(post=post, author=request.user)
            vote.value += value
            if vote.value == 2:
                vote.value = 1
            elif vote.value == -2:
                vote.value = -1
            vote.save()
        else:
            form = VoteForm(request.POST)
            if form.is_valid():
                vote = form.save(commit=False)
                vote.author = request.user
                vote.post = post
                vote.value = value
                vote.save()
        # return redirect('post:detail', pk=post.pk)
        return HttpResponse(post.get_rating())
