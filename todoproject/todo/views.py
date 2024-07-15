# todo/views.py
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Todo
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.decorators import login_required
from django.contrib import auth, messages
from django.http import HttpResponse
# Create your views here.
def signup(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        username = request.POST.get('username', '')
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')
        password2 = request.POST.get('password2', '')
        if not all([username, email, password, password2]):
            messages.error(request, 'Please fill in all required fields')
            return redirect('signup')

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already exists')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
                user.save()
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                new_profile.save()
                return redirect('settings')
        else:
            messages.info(request, 'Password not matching')
            return redirect('signup')
    else:
        return render(request, 'signup.html')

def signin(request):

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('signin')
    else:    
        return render(request, 'signin.html')


@login_required
class TodoListView(ListView):
    model = Todo
    template_name = 'todo/todo_list.html'
@login_required
class TodoDetailView(DetailView):
    model = Todo
    template_name = 'todo/todo_detail.html'
@login_required
class TodoCreateView(CreateView):
    model = Todo
    template_name = 'todo/todo_form.html'
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('todo_list')

class TodoUpdateView(UpdateView):
    model = Todo
    template_name = 'todo/todo_form.html'
    fields = ['title', 'description', 'completed']
    success_url = reverse_lazy('todo_list')

class TodoDeleteView(DeleteView):
    model = Todo
    template_name = 'todo/todo_confirm_delete.html'
    success_url = reverse_lazy('todo_list')
