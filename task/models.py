from django.db import models
from accounts.models import Users
from config import settings


class Project(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(blank=True, null=True)
    start_date = models.DateTimeField()

class Tasks(models.Model):
    class StatusOption(models.TextChoices):
        Pending = 'pending', 'Pending'
        In_Progress = 'in_pregress', 'In progress'
        Completed = 'completed', 'Completed'

    title = models.CharField(max_length=100, null=False, blank=False)
    project = models.ForeignKey('Project', on_delete=models.CASCADE)
    assign_to = models.ManyToManyField(settings.AUTH_USER_MODEL)
    description = models.TextField()
    status = models.CharField(choices=StatusOption, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)