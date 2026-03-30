from django.db import models
from django.utils import timezone


class IssueReport(models.Model):
    ISSUE_TYPES = [
        ('water', 'Water Leak'),
        ('electricity', 'Electricity Fault'),
        ('pothole', 'Pothole'),
        ('waste', 'Waste Collection'),
    ]

    STATUS_CHOICES = [
        ('submitted', 'Submitted'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('rejected', 'Rejected'),
    ]

    issue_type = models.CharField(max_length=20, choices=ISSUE_TYPES)
    description = models.TextField()
    location = models.CharField(max_length=255, blank=True, default='')
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    photo = models.ImageField(upload_to='issue_photos/', null=True, blank=True)
    voice_note = models.FileField(upload_to='voice_notes/', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='submitted')
    submitted_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-submitted_at']

    def __str__(self):
        return f"{self.get_issue_type_display()} at {self.location} [{self.status}]"

    def get_status_color(self):
        colors = {
            'submitted': 'blue',
            'in_progress': 'amber',
            'completed': 'green',
            'rejected': 'red',
        }
        return colors.get(self.status, 'gray')