from django.shortcuts import get_object_or_404, redirect, render_to_response

from comment.forms import NewCommentForm

from post.models import Post


def new_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = NewCommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
    return redirect('post:detail', pk=post.pk)


def comment_list(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render_to_response('comment/comments.html', {'post': post})

# class CommentsListView(ListView):
#     model = Comment
#     related_post = None
#     template_name = 'comment/comments.html'
#
#     def get_queryset(self):
#         return Comment.objects.filter()

