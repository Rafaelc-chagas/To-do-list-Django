from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from tasks.models import Task
from tasks.forms import TaskModelForm


class TaskListView(ListView):
    model = Task
    template_name = 'tasks.html'
    context_object_name = 'tasks'

    def get_queryset(self):
        tasks = super().get_queryset().order_by('title')
        search = self.request.GET.get('search')
        if search:
            tasks = tasks.filter(title__icontains=search)
        return tasks


class NewTaskCreateView(CreateView):
    model = Task
    form_class = TaskModelForm
    template_name = 'new_task.html'
    success_url = '/tasks/'


class UpdateTaskView(UpdateView):
    model = Task
    form_class = TaskModelForm
    template_name = 'task_update.html'
    success_url = '/tasks/'


class DeleteTaskView(DeleteView):
    model = Task
    template_name = 'task_delete.html'
    success_url = '/tasks/'


class DetailTaskView(DetailView):
    model = Task
    template_name = 'task_detail.html'


class AboutTemplateView(TemplateView):
    template_name = 'about.html'


class ContactTemplateView(TemplateView):
    template_name = 'contact.html'
