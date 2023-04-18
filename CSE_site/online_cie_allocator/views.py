from django.shortcuts import render, redirect, HttpResponse
from django.urls import reverse
from .decorators import allowed_users

from openpyxl import Workbook, load_workbook
from openpyxl.writer.excel import save_virtual_workbook

from CSE_site.models import Exam, Course
from .models import Assigned_Exam_Room
from authentication.models import Student

def exam_allocator(req):
    if req.user.groups.filter(name="Student"):
        return redirect(reverse("exam_allocator_student_dashboard"))
    elif req.user.groups.filter(name="Office"):
        return redirect(reverse("exam_allocator_office_dashboard"))
    elif req.user.groups.filter(name="Faculty"):
        return redirect(reverse("exam_allocator_faculty_view"))
    else:
        return HttpResponse("You don't have access to this page")

@allowed_users(["Faculty"])
def faculty_view(req):
    return HttpResponse("You don't have access to this page")

@allowed_users(["Office"])
def office_dashboard(req):
    if req.method == "POST":
        # TODO: check for any exception here
        semester = int(req.POST.get("semester"))
        
        return redirect(reverse("exam_allocator_office_semester_view", args=(semester,)))
    
    return render(req, "exam_allocator_office_dashboard.html", {})

@allowed_users(["Office"])
def office_semester_view(req, sem):
    return render(req, "exam_allocator_office_semester_view.html", {"sem": sem})

# @allowed_users(["Office"])
def office_download_template(req, semester):
    if req.method == "POST":
        wb = Workbook()

        for course_object in Course.objects.filter(sem=semester):
            wb.create_sheet(course_object.code)
            ws = wb[course_object.code]
            ws.append(["USN", "Room"])
            for i, student_object in enumerate(Student.objects.filter(courses=course_object)):
                ws[f"A{i+2}"] = student_object.usn

        wb.remove_sheet(wb.get_sheet_by_name("Sheet"))
        excel_data = save_virtual_workbook(wb)
        response = HttpResponse(excel_data, content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = f'attachment; filename="{semester}_Sem_Exam_Allocation.xlsx"'

        return response

@allowed_users(["Office"])
def office_upload(req):
    if req.method == "POST":
        exam_title = req.POST.get("exam")
        try:
            excel_file = req.FILES["excel_file"]
        except Exception as e:
            return HttpResponse(f"Please select a file before uploading {e}")
        
        if not excel_file.name.endswith("xlsx"):
            return HttpResponse("Please upload a .xlsx file")
        
        wb = load_workbook(excel_file)
        for ws_name in wb.sheetnames:
            ws = wb[ws_name]
            course = Course.objects.get(code=ws_name)
            exam = Exam.objects.get(title=exam_title)

            rows_iter = ws.iter_rows()
            next(rows_iter)
            for row in rows_iter:
                print(row[0].value, type(row[0].value))
                student = Student.objects.get(usn=row[0].value)
                room_info = Assigned_Exam_Room(stud_id=student, course_id = course, exam_id=exam, room_number=row[1].value)
                room_info.save()
                


@allowed_users(["Student"])
def student_dashboard(req):
    if req.method == "POST":
        examTitle = req.POST.get("exams")

        if examTitle not in [exam.title for exam in Exam.objects.all()]:
            return HttpResponse("Select a valid exam!")
        
        exam = Exam.objects.get(title=examTitle)
        stud = Student.objects.get(email=req.user.email)

        rooms = Assigned_Exam_Room.objects.filter(stud_id=stud, exam_id=exam)
        rooms_data = []
        for room in rooms:
            rooms_data.append([room.course_id.code, room.room_number])

        return render(req, "exam_allocator_student_dashboard.html", {"rooms_data": rooms_data})

    return render(req, "exam_allocator_student_dashboard.html", {})