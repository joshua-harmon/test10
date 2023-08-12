from django.db import models
from django.contrib.auth.models import User
from django.template import defaultfilters

# Create your models here.
class Category(models.Model):
  title = models.CharField(max_length=255)

  class Meta:
    ordering = ('title',)
    
class Job(models.Model):
  category = models.ForeignKey(Category, related_name='jobs', on_delete=models.CASCADE)
  title = models.CharField(max_length=255)
  description = models.CharField(max_length=3000, blank=True, null=True)
  position_salary = models.CharField(max_length=255)
  position_location = models.CharField(max_length=255)
  company_name = models.CharField(max_length=255)
  company_location = models.CharField(max_length=255)
  company_email = models.EmailField(max_length=255)
  created_at = models.DateTimeField(auto_now=True)
  created_by = models.ForeignKey(User, related_name='jobs', on_delete=models.CASCADE)
  
  def created_at_formatted(self):
    return defaultfilters.date(self.created_at, 'M d, Y')
  
  class Meta:
    ordering = ('-created_at',)
    
