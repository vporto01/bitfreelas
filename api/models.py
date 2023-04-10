from django.db import models
from accounts.models import CustomUser

class Skill(models.Model):

    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Client(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    avatar = models.ImageField(blank=True, null=True)
    company_name = models.CharField(max_length=100, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.first_name

class Freelancer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    description = models.CharField(max_length=30, blank=True, null=True)
    avatar = models.ImageField(blank=True, null=True)
    skills = models.ManyToManyField(Skill, blank=True)
    hourly_rate = models.DecimalField(max_digits=10, decimal_places=2)
    bio = models.TextField(blank=True, null=True)
    portfolio = models.URLField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.user.first_name

class Wallets(models.Model):
    private_key = models.CharField(max_length=2000, blank=False, null=False)
    private_key_wif = models.CharField(max_length=2000, blank=False, null=False)
    public_key_hex = models.CharField(max_length=200, blank=False, null=False)
    address = models.CharField(max_length=200, blank=False, null=False)
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = ('Wallet')
        verbose_name_plural = ('Wallets')

    def __str__(self):
        return f"{self.user}"
