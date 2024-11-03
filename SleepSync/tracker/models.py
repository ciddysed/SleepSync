from django.db import models

class ProgressTracking(models.Model):  # Check this name
    progress_id = models.AutoField(primary_key=True)
    date = models.DateField()
    goal = models.CharField(max_length=50)
    progress_value = models.FloatField()

class SleepTrack(models.Model):
    tracking_id = models.AutoField(primary_key=True)
    date = models.DateField()
    sleep_duration = models.TimeField()
    sleep_quality = models.CharField(max_length=15)
    sleep_stages = models.CharField(max_length=15)

    schedule_id = models.IntegerField() 

    def __str__(self):
        return f"{self.date} - {self.sleep_quality}"
