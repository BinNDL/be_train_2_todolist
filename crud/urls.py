from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("<int:id>/", views.task_detail, name="task_detail"),
    path("add/", views.add_task, name="add_task"),
    path("delete/", views.delete_task, name="delete_task"),
    path("update/", views.update_task, name="update_task"),
    path('search_tasks/', views.search_tasks, name='search_tasks'),
    path('filter_tasks/', views.filter_tasks, name='filter_tasks'),
]
