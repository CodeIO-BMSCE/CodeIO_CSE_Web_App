from django.shortcuts import render, HttpResponse
from .decorators import allowed_users

from CSE_site.models import Exam
from .models import Assigned_Exam_Room
from authentication.models import Student

def office_view(req):
    return render(req, "cie_allocator_office.html", {})

@allowed_users(["Student"])
def student_view(req):
    if req.method == "POST":
        examTitle = req.POST.get("exams")

        if examTitle not in [exam.title for exam in Exam.objects.all()]:
            return HttpResponse("Select a valid exam!")
        
        exam = Exam.objects.get(title=examTitle)
        stud = Student.objects.get(email=req.user.email)

        rooms = Assigned_Exam_Room.objects.filter(stud_id=stud, exam_id=exam)
        rooms_data = []
        for room in rooms:
            rooms_data.append([room.course_id.code, room.room_name.roomName])

        return render(req, "cie_allocator_student.html", {"rooms_data": rooms_data})

    return render(req, "cie_allocator_student.html", {})