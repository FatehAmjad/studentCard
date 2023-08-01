from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.http import JsonResponse
from .models import studentDetails 
from .forms import myForm
from io import BytesIO
from barcode import EAN8
from barcode.writer import SVGWriter
import os
def studentForm(request):
    if request.method == "POST":
        sID = request.POST['studentID']
        sName = request.POST['studentName']
        sCourse = request.POST['courseEnrolled']
        startingDate = request.POST['dateEnrolled']
        sImages = request.FILES.get('sImages')
        
        file_extension = os.path.splitext(sImages.name)[1].lower()
        new_image_name = f"{sID}{file_extension}"
        
        studentDetails.objects.create(student_id = sID, 
                                      student_name = sName,
                                      course = sCourse, 
                                      begin_date = startingDate,
                                      studentImages = f"images/{new_image_name}")
        
        image_path = os.path.join("media", "images", new_image_name)
        
        with open(image_path, "wb") as f:
            for chunk in sImages.chunks():
                f.write(chunk)
        
        with open(f"../studentID/media/cardBarcode/{sID}.svg", "wb") as f:
            EAN8(sID, writer=SVGWriter()).write(f)
            
        form = myForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
    else:
        form = myForm()
    
    context = {"form": form}
    return render(request, "application/Form.html", context)

def database_view(request):
    context = {
        "sList" : studentDetails.objects.all()
    }
    return render(request, 'application/Database.html', context)
    
def update_status(request):
    if request.method == "POST" and request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        student_id = request.POST.get("student_id")
        status = request.POST.get("status")

        try:
            student = studentDetails.objects.get(student_id=student_id)
            student.status = status
            student.save()
            return JsonResponse({"message": "Status updated successfully."})
        except studentDetails.DoesNotExist:
            return JsonResponse({"error": "Student not found."}, status=404)
    else:
        return JsonResponse({"error": "Invalid request."}, status=400)
