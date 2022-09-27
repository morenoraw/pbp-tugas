# TODO: Implement Routings Here
from django.urls import path
from todolist.views import delete_task, marker, show_todolist, create_task
from todolist.views import register, login_user, logout_user

app_name = 'todolist'

urlpatterns = [
    path('', show_todolist, name='show_todolist'),
    path('login/', login_user, name='login'),
    path('register/', register, name='register'),
    path('create-task/', create_task, name='create_task'),
    path('logout/', logout_user, name='logout'),
    path('marker/<int:id>', marker, name='marker'),
    path('delete/<int:id>', delete_task, name='delete')
]