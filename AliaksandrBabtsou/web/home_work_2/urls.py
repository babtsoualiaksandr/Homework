from django.urls import path

from . import views

urlpatterns = [
    path('tasks/', views.tasks, name='tasks'),
    path('tasks/<int:task_id>/detail/', views.detail, name='detail'),
    path('', views.index, name='index'),
]