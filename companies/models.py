from django.db import models
from accounts.models import User

class Company(models.Model):
    company_name = models.CharField(max_length=255)
    company_address = models.TextField(null=True, blank=True)  # Optional field
    company_email = models.EmailField(unique=True)
    company_phone = models.CharField(max_length=50, null=True, blank=True)  # Optional field
    users = models.ManyToManyField(User, related_name="companies")

    class Meta:
        ordering = ["company_name"]

    def __str__(self):
        return self.company_name
