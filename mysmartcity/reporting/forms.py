from django import forms
from .models import IssueReport


class IssueReportForm(forms.ModelForm):
    class Meta:
        model = IssueReport
        fields = ['issue_type', 'description', 'location', 'latitude', 'longitude', 'photo', 'voice_note']
        widgets = {
            'issue_type': forms.HiddenInput(),
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
            'description': forms.Textarea(attrs={'rows': 4}),
            'location': forms.TextInput(),
            'photo': forms.FileInput(attrs={'accept': 'image/*'}),
            'voice_note': forms.FileInput(attrs={'accept': 'audio/*'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['location'].required = False
        self.fields['photo'].required = False
        self.fields['voice_note'].required = False
        self.fields['latitude'].required = False
        self.fields['longitude'].required = False
        self.fields['description'].required = True