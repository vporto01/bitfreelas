from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    deadline = models.DateField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    skills_required = models.CharField(max_length=500)
    project_type_choices = [
        ('fixed', 'Fixed'),
        ('hourly', 'Hourly'),
    ]
    project_type = models.CharField(max_length=10, choices=project_type_choices)
    project_status_choices = [
        ('open', 'Open'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]
    project_status = models.CharField(max_length=15, choices=project_status_choices)
    # client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_projects')
    # freelancer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='freelancer_projects')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    attachments = models.FileField(upload_to='attachments/', null=True, blank=True)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE)
    proposal_count = models.PositiveIntegerField(default=0)
    currency = models.CharField(max_length=10, default='USD')
    location_preference = models.CharField(max_length=200, null=True, blank=True)

