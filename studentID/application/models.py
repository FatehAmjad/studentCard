from django.db import models
from datetime import date

class studentDetails(models.Model):
    student_id = models.IntegerField()
    student_name = models.CharField(max_length=20)
    course = models.CharField(max_length=20)
    begin_date = models.DateField()
    STATUS_CHOICES = [
        ('Enrolled', 'Enrolled'),
        ('Withdrawn', 'Withdrawn'),
        ('on-leave', 'On Leave'),
        ('Paused', 'Paused'),
        ('Terminated', 'Terminated'),
        ('Graduated', 'Graduated'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, blank=True, null=True)
    studentImages = models.ImageField(upload_to='images/')
    CARD_STATUS_CHOICES = [
        ('Collected', 'Collected'),
        ('Lost', 'Lost'),
        ('Renewed', 'Renewed'),
        ('In-process', 'In-process')
    ]
    card_status = models.CharField(max_length=20, choices=CARD_STATUS_CHOICES, blank=True, null=True)
    
