from django.db import models
from django.contrib.auth.models import User

# class Skill(models.Model):

#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# class Currency(models.Model):

#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# class Client(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     company_name = models.CharField(max_length=100, blank=True, null=True)
#     website = models.URLField(blank=True, null=True)
#     phone_number = models.CharField(max_length=15, blank=True, null=True)
#     bio = models.TextField(blank=True, null=True)

#     def __str__(self):
#         return self.user.username

# class Freelancer(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     skills = models.ManyToManyField(Skill, blank=True)
#     hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
#     bio = models.TextField(blank=True, null=True)
#     portfolio = models.URLField(blank=True, null=True)
#     phone_number = models.CharField(max_length=15, blank=True, null=True)

#     def __str__(self):
#         return self.user.username

# class Category(models.Model):
#     name = models.CharField(max_length=100, default="Categoria padrão")

#     def __str__(self):
#         return self.name


# #-------------------------------------------
# class Project(models.Model):
#     title = models.CharField(max_length=200)
#     description = models.TextField()
#     deadline = models.DateField()
#     budget = models.DecimalField(max_digits=10, decimal_places=2)
#     skills_required = models.ManyToManyField(Skill, blank=True)
#     project_type_choices = [
#         ('fixed', 'Fixed'),
#         ('hourly', 'Hourly'),
#     ]
    
#     project_type = models.CharField(max_length=10, choices=project_type_choices)
#     hourly_rate = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
#     project_status_choices = [
#         ('open', 'Open'),
#         ('in_progress', 'In Progress'),
#         ('completed', 'Completed'),
#         ('cancelled', 'Cancelled'),
#     ]
#     project_status = models.CharField(max_length=15, choices=project_status_choices)
#     client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_projects')
#     # freelancer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='freelancer_projects')
#     date_created = models.DateTimeField(auto_now_add=True)
#     date_updated = models.DateTimeField(auto_now=True)
#     attachments = models.FileField(upload_to='attachments/', null=True, blank=True)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)
#     proposal_count = models.PositiveIntegerField(default=0)
#     currency = models.ForeignKey(Currency, on_delete=models.CASCADE)
#     location_preference = models.CharField(max_length=200, null=True, blank=True)

#     def __str__(self):
#         return self.title
