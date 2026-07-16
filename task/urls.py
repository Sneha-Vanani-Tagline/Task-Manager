from django.urls import path
from task import views

app_name = 'task'

urlpatterns = [
    path('list/', views.TaskListView.as_view())
]