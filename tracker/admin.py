from django.contrib import admin
from .models import Company, Job, Application, ApplicationStatusHistory

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'website')

@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'source')
    list_filter = ('source', 'company')

class ApplicationHistoryInline(admin.TabularInline):
    model = ApplicationStatusHistory
    extra = 0
    readonly_fields = ('old_status', 'new_status', 'changed_at')

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('job', 'company', 'user', 'status', 'date_applied', 'next_follow_up_on')
    list_filter = ('status', 'company')
    inlines = [ApplicationHistoryInline]
