from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views import generic

from app.forms import TaskForm
from app.models import Task, Tag


class Home(generic.ListView):
    model = Task
    queryset = Task.objects.all()
    template_name = "app/home.html"


class TaskCreateView(generic.CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("app:home")


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("app:home")


class TaskUpdateView(generic.UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("app:home")


class TagListView(generic.ListView):
    model = Tag
    queryset = Tag.objects.all()


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("app:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("app:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("app:tag-list")


def mark_complete_or_undo(request, pk):
    task = Task.objects.get(id=pk)
    if task.is_done is False:
        task.is_done = True
    else:
        task.is_done = False
    task.save()
    return HttpResponseRedirect(reverse_lazy("app:home"))
