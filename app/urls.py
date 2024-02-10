"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks.views import TaskListView, NewTaskCreateView, UpdateTaskView, DeleteTaskView, DetailTaskView, AboutTemplateView, ContactTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tasks/', TaskListView.as_view(), name='tasks'),
    path('new_task/', NewTaskCreateView.as_view(), name='new_task'),
    path('task/<int:pk>/update', UpdateTaskView.as_view(), name='task_update'),
    path('task/<int:pk>/delete', DeleteTaskView.as_view(), name='task_delete'),
    path('task/<int:pk>/detail', DetailTaskView.as_view(), name='task_detail'),
    path('about/', AboutTemplateView.as_view(), name='about'),
    path('contact', ContactTemplateView.as_view(), name='contact'),
]
