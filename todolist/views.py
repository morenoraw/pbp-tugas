import datetime
from todolist.models import Task
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.forms import Form
from todolist.taskform import TaskAdd

# TODO: Create your views here.

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    data_task_todolist = Task.objects.filter(user = request.user)
    context = {
        'list_task': data_task_todolist
    }
    return render(request, "todolist.html", context)

@login_required(login_url='/todolist/login/')
def create_task(request):
    form = TaskAdd(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            Task.objects.create(title=title, description=description, date=datetime.datetime.now(), user=request.user)
            return redirect('todolist:show_todolist')
        else:
            form = TaskAdd()
    context = {'form': form}
    return render(request, "create_task.html", context)

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("todolist:show_todolist"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def marker(request, id):
    task = Task.objects.get(id = id)
    task.is_finished = not(task.is_finished)
    task.save()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def delete_task(request, id):
    task = Task.objects.get(id = id)
    task.delete()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login/')
def show_json(request):
    current_user = request.user
    data = Task.objects.filter(user=current_user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/todolist/login/')
def show_todolist_ajax(request):
    context = {
        'user': request.user
    }
    return render(request, 'todolist_ajax.html', context)

@login_required(login_url='/todolist/login/')
def create_task_ajax(request):
    if request.method == 'POST':
        new_task = Task(
            user = request.user,
            title = request.POST.get('title_ajax'),
            description = request.POST.get('description_ajax')
        )
        new_task.save()
        return HttpResponse(serializers.serialize('json', [new_task,]), content_type='application/json')
    return HttpResponse('')