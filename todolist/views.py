from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, DeleteView, UpdateView

from todolist.forms import TaskForm, TagForm
from todolist.models import Task, Tag


class TaskListView(ListView):
    model = Task
    template_name = "todolist/task_list.html"
    context_object_name = "tasks"
    paginate_by = 10
    queryset = Task.objects.prefetch_related("tags")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        uncompleted_tasks_count = Task.objects.filter(
            is_complete=False).count()
        context["uncompleted_tasks_count"] = uncompleted_tasks_count

        return context

    def post(self, request, *args, **kwargs):
        task_id = request.POST.get("task_id")
        if task_id:
            task = Task.objects.get(pk=task_id)
            task.is_complete = not task.is_complete
            task.save()
        return redirect("todolist:task-list")


class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todolist:task-list")


class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy("todolist:task-list")


class TaskDeleteView(DeleteView):
    model = Task
    success_url = reverse_lazy("todolist:task-list")


class TagListView(ListView):
    model = Tag
    template_name = "todolist/tag_list.html"
    context_object_name = "tags"
    paginate_by = 10


class TagCreateView(CreateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("todolist:tag-list")


class TagUpdateView(UpdateView):
    model = Tag
    form_class = TagForm
    success_url = reverse_lazy("todolist:tag-list")


class TagDeleteView(DeleteView):
    model = Tag
    success_url = reverse_lazy("todolist:tag-list")
