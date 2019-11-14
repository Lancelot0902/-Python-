# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def logout_view(request):
    """ log out """
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))


def register(request):
    """ logup """
    if request.method != 'POST':
        # show empty form to logup
        form = UserCreationForm(data=request.POST)

    else:
        # use filled form
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # make user login automatically and turn to main page
            authenticated_user = authenticate(username=new_user.username,
                                              password=request.POST['password1'])
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))

    context = {'form': form}
    return render(request, 'users/register.html', context)
