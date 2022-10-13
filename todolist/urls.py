# TODO: Implement Routings Here
from django.urls import path
from todolist.views import create_task_ajax, delete_task, marker, show_todolist, create_task, register, login_user, logout_user, show_json, show_todolist_ajax

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('create-task/', create_task, name='create_task'),
    path('logout/', logout_user, name='logout'),
    path('marker/<int:id>', marker, name='marker'),
    path('delete/<int:id>', delete_task, name='delete'),
    path('json/', show_json, name='show_json'),
    path('ajax/', show_todolist_ajax, name='show_todolist_ajax'),
    path('add/', create_task_ajax, name='create_task_ajax')
]