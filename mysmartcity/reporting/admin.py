from django.contrib import admin
from .models import IssueReport


@admin.register(IssueReport)
class IssueReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'issue_type', 'location', 'status', 'submitted_at')
    list_filter = ('status', 'issue_type')
    search_fields = ('description', 'location')
    list_editable = ('status',)
    ordering = ('-submitted_at',)
    readonly_fields = ('submitted_at', 'updated_at')

# Register your models here.
