from django import forms 
from .models import studentDetails

class myForm(forms.ModelForm):
    class Meta:
        model = studentDetails
        fields = ["student_id", "student_name", "course", "begin_date", "studentImages"]
        labels = {"student_id" : "ID", "student_name" : "Name", "course": "Course Name", "begin_date": "Date joined", "studentImages" : 'Student image'}
