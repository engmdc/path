from django.db import models

class EventType(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Event Types"

class Facility(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    additional_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Facilities"


class Hall(models.Model):
    company = models.CharField(max_length=100, default="NAGAAD HALLS")
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    capacity = models.IntegerField(default=0)
    price_per_guest = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    facilities = models.TextField(blank=True, null=True)
    income_account = models.CharField(max_length=100)
    extra_income_account = models.CharField(max_length=100)
    receivable_account = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
