# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from .models import Topic, Entry

from .forms import TopicForm, EntryForm

from django.shortcuts import render

from django.http import HttpResponseRedirect, Http404

from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required


# Create your views here.
def index(request):
    """ home page of learning_logs """
    return render(request, 'learning_logs/index.html')


@login_required
def topics(request):
    """ show topics """
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics':topics}
    return render(request, 'learning_logs/topics.html',context)


@login_required
def topic(request,topic_id):
    """ show all items of one topic """
    topic = Topic.objects.get(id=topic_id)
    # make sure the entry is belonged with current user
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)


@login_required
def new_topic(request):
    """ add new topic """
    if request.method != 'POST':
        # GET,create a new form
        form = TopicForm()
    else:
        # POST,use data
        form = TopicForm(request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)


@login_required
def new_entry(request, topic_id):
    """ add new entry in the topic """
    topic = Topic.objects.get(id=topic_id)
    if topic.owner != request.user:
        raise Http404
    if request.method != 'POST':
        # GET,create new form
        form = EntryForm()
    else:
        # POST,use data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)


@login_required
def edit_entry(request, entry_id):
    """ edit current entry """
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        # GET show current entry
        form = EntryForm(instance=entry)
    else:
        # POST use data
        form = EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topic',args=[topic.id]))

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)
