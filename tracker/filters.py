import django_filters as df
from django import forms
from django.db import models
from .models import Application, Company

class ApplicationFilter(df.FilterSet):
    status = df.ChoiceFilter(
        choices=Application.Status.choices,
        label='Status',
        empty_label='All statuses',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    company = df.ModelChoiceFilter(
        queryset=Company.objects.all().order_by('name'),
        label='Company',
        empty_label='All companies',
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    q = df.CharFilter(
        method='filter_q', label='Search',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search title or notes'})
    )

    class Meta:
        model = Application
        fields = ['status', 'company']

    def filter_q(self, queryset, name, value):
        if not value:
            return queryset
        return queryset.filter(
            models.Q(job__title__icontains=value) |
            models.Q(notes__icontains=value)
        )
