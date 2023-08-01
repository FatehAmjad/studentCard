from django.contrib import admin
from django import forms
from .models import studentDetails
from import_export.admin import ExportActionMixin

class studentListForm(forms.ModelForm):
    class Meta:
        model = studentDetails
        fields = "__all__"

class studentList(ExportActionMixin, admin.ModelAdmin):
    form = studentListForm
    list_display = ("student_id", "student_name", "course", "begin_date", "studentImages", "status")
    list_editable = ["status"]
    
    def save_model(self, request, obj, form, change):
        # Save the student instance with the updated status
        obj.status = form.cleaned_data['status']
        obj.save(update_fields=['status'])

admin.site.register(studentDetails, studentList)