from django.http import HttpResponseForbidden
from django.urls import reverse
from django.views.generic import DetailView
from django.views.generic import UpdateView

from core.models import User
from rating.models import Vote


class UserUpdateView(UpdateView):
    model = User
    template_name = 'user_edit.html'
    fields = (
        'username',
        'first_name',
        'last_name',
        'email',
        'avatar',
    )

    def get_object(self, queryset=None):
        return self.request.user                # TODO: check to anonymous user

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj != self.request.user:
            return HttpResponseForbidden('forbidden')
        return super(UserUpdateView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('user:user_view', kwargs={'pk': self.object.id})


class UserProfileView(DetailView):
    model = User
    template_name = 'user_profile.html'
    queryset = User.objects.all()
    context_object_name = 'selected_user'

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        votes_up = Vote.objects.filter(author=self.get_object(), value=1).count()
        votes_down = Vote.objects.filter(author=self.get_object(), value=-1).count()
        context['votes_up'] = votes_up
        context['votes_down'] = votes_down
        return context
