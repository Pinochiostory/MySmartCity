from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import IssueReportForm
from .models import IssueReport


def report_issue(request):
    if request.method == 'POST':
        print("=== FORM SUBMITTED ===")
        print("POST data:", request.POST)

        form = IssueReportForm(request.POST, request.FILES)

        print("Form is valid:", form.is_valid())
        if not form.is_valid():
            print("Form errors:", form.errors)

        if form.is_valid():
            report = form.save()
            print("Saved report ID:", report.id)
            messages.success(request, f'Report submitted! Reference ID: #{report.id}')
            return redirect('track_issue')
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'Error in {field}: {error}')
    else:
        form = IssueReportForm()

    return render(request, 'reporting/report_issue.html', {'form': form})
