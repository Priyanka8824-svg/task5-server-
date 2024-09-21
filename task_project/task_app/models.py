from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()

# Create your models here.
class Task(models.Model):
    status = {'pending':'pending', 'completed':'completed', 'in_progress':'in_progress'}

    task_name = models.CharField(max_length=20)
    task_description = models.TextField()
    task_status = models.CharField(max_length=20, choices=status, default='pending')
    task_assigned_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigner')
    task_assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assignee')
    task_assigned_date = models.DateTimeField(auto_now_add=True)
    task_completed_date = models.DateTimeField(null=True, blank=True)
    task_deadline = models.DateTimeField()