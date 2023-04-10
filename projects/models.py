from django.db import models
from api.models import CustomUser

class Projects(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    short_description = models.CharField(max_length=30, blank=True, null=True, verbose_name="Short description")
    full_description = models.TextField(blank=True, null=True, verbose_name="Full description")
    date_posted = models.DateField(auto_now_add=True, blank=True, null=True)
    type_choices = [
        ('fixed', 'Fixed'),
        ('hourly', 'Hourly'),
    ]
    type = models.CharField(max_length=6, choices=type_choices)
    budget = models.FloatField()
    currency_choices = [
        ('btc', 'BTC'),
    ]
    currency = models.CharField(max_length=5, choices=currency_choices, default='BTC')

    class Meta:
        verbose_name = ('Project')
        verbose_name_plural = ('Projects')
    
    def __str__(self) -> str:
        return f'{self.short_description}'
