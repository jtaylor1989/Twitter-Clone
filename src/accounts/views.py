from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.views.generic import View, DetailView

from .models import UserProfile


User = get_user_model()


class UserDetailView(DetailView):
    template_name = 'accounts/user_detail.html'
    queryset = User.objects.all()

    def get_object(self):
        '''
        override the get_object method to lookup
        for a username parameter; defaults to pk or slug
        '''
        return get_object_or_404(
                                User,
                                username__iexact=self.kwargs.get('username')
                                )

    def get_context_data(self, *args, **kwargs):
        context = super(UserDetailView, self).get_context_data(*args, **kwargs)
        following = UserProfile.objects.is_following(self.request.user, self.get_object())
        context['following'] = following
        context['recommended'] = UserProfile.objects.recommended(self.request.user)
        return context


class UserFollowView(View):
    '''
    follow toggle based on a url
    '''

    def get(self, request, username, *args, **kwargs):
        toggle_user = get_object_or_404(User, username__iexact=username)
        if request.user.is_authenticated():
            is_following = UserProfile.objects.toggle_follow(request.user, toggle_user)
        return redirect("profiles:detail", username=username)
