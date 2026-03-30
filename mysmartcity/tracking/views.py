from django.shortcuts import render
from reporting.models import IssueReport


def track_issue(request):
    status_filter = request.GET.get('status', 'all')
    search_query = request.GET.get('search', '').strip()

    issues = IssueReport.objects.all()

    if status_filter and status_filter != 'all':
        issues = issues.filter(status=status_filter)

    if search_query:
        issues = issues.filter(
            description__icontains=search_query
        ) | issues.filter(
            location__icontains=search_query
        )

    total = IssueReport.objects.count()
    submitted_count = IssueReport.objects.filter(status='submitted').count()
    in_progress_count = IssueReport.objects.filter(status='in_progress').count()
    completed_count = IssueReport.objects.filter(status='completed').count()

    context = {
        'issues': issues,
        'status_filter': status_filter,
        'search_query': search_query,
        'total': total,
        'submitted_count': submitted_count,
        'in_progress_count': in_progress_count,
        'completed_count': completed_count,
    }
    return render(request, 'tracking/track_issue.html', context)