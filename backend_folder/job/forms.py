from django import forms
from .models import Job

class JobForm(forms.ModelForm):
  class Meta:
    model = Job
    fields = (
      'category',
      'title',
      'description',
      'position_salary',
      'position_location',
      'company_name',
      'company_location',
      'company_email',
    )