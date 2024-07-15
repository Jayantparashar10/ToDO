
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import ToDo
from django.urls import reverse_lazy

class ToDoListView(LoginRequiredMixin, ListView):
    model = ToDo
    context_object_name = 'todos'
    template_name = 'todo/todo_list.html'

    def get_queryset(self):
        return ToDo.objects.filter(user=self.request.user)

class ToDoDetailView(LoginRequiredMixin, DetailView):
    model = ToDo
    template_name = 'todo/todo_detail.html'

class ToDoCreateView(LoginRequiredMixin, CreateView):
    model = ToDo
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('todo_list')
    template_name = 'todo/todo_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ToDoUpdateView(LoginRequiredMixin, UpdateView):
    model = ToDo
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('todo_list')
    template_name = 'todo/todo_form.html'

class ToDoDeleteView(LoginRequiredMixin, DeleteView):
    model = ToDo
    success_url = reverse_lazy('todo_list')
    template_name = 'todo/todo_confirm_delete.html'
