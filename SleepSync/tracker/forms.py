from django import forms
from .models import ProgressTracking, SleepTrack

class ProgressTrackingForm(forms.ModelForm):
    class Meta:
        model = ProgressTracking
        fields = ['date', 'goal', 'progress_value']

class SleepTrackForm(forms.ModelForm):
    class Meta:
        model = SleepTrack
        fields = ['date', 'sleep_duration', 'sleep_quality', 'sleep_stages', 'schedule_id']
