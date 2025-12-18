from django.conf import settings
from django.db import models
from django.utils import timezone

class Company(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField(blank=True)
    def __str__(self):
        return self.name

class Job(models.Model):
    SOURCE_CHOICES = [
        ('linkedin', 'LinkedIn'),
        ('company', 'Company Site'),
        ('other', 'Other'),
    ]
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='jobs')
    title = models.CharField(max_length=200)
    location = models.CharField(max_length=200, blank=True)
    job_link = models.URLField(blank=True)
    source = models.CharField(max_length=20, choices=SOURCE_CHOICES, default='other')
    salary_range = models.CharField(max_length=100, blank=True)
    def __str__(self):
        return f"{self.title} @ {self.company.name}"

class Application(models.Model):
    class Status(models.TextChoices):
        SAVED = 'saved', 'Saved'
        APPLIED = 'applied', 'Applied'
        INTERVIEW = 'interview', 'Interview'
        OFFER = 'offer', 'Offer'
        REJECTED = 'rejected', 'Rejected'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='applications')
    company = models.ForeignKey(Company, on_delete=models.PROTECT)
    job = models.ForeignKey(Job, on_delete=models.PROTECT)

    status = models.CharField(max_length=20, choices=Status.choices, default=Status.SAVED)
    date_applied = models.DateField(null=True, blank=True)
    next_follow_up_on = models.DateField(null=True, blank=True)
    notes = models.TextField(blank=True)
    resume_version = models.CharField(max_length=100, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def is_follow_up_due(self):
        return self.next_follow_up_on and self.next_follow_up_on <= timezone.localdate()

    def __str__(self):
        return f"{self.job.title} @ {self.company.name}"

class ApplicationStatusHistory(models.Model):
    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='history')
    old_status = models.CharField(max_length=20, choices=Application.Status.choices)
    new_status = models.CharField(max_length=20, choices=Application.Status.choices)
    changed_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-changed_at']
