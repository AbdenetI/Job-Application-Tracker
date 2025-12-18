from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Application, Company, Job

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ["name", "website"]

class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ["company", "title", "location", "job_link", "source", "salary_range"]

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = [
            "company", "job", "status", "date_applied",
            "next_follow_up_on", "notes", "resume_version",
        ]
        widgets = {
            'date_applied': forms.DateInput(attrs={'type': 'date'}),
            'next_follow_up_on': forms.DateInput(attrs={'type': 'date'}),
        }
