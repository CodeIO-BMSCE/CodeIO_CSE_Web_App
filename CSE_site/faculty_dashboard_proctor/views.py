from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Faculty
from student_dashboard_proctor.models import Student, StudentDetail, Sem, Fastrack, courseRequest
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.conf import settings
import openpyxl
import pandas as pd

# Create your views here.
@login_required
def dashboard(request):
    faculty = Faculty.objects.get(email=request.user.email)
    students = Student.objects.filter(proctor_id=faculty)
    context = {'faculty': faculty, 'students': students}
    return render(request, 'faculty_dashboard_proctor/dashboard.html', context)

def sendFillMail(request, message, name, emails):
    template = render_to_string('faculty_dashboard_proctor/send_fill.html', {'message': message, 'name': name})
    email = EmailMessage(
                message,
                template,
                settings.EMAIL_HOST_USER,
                [emails],
                # fail_silently=False,
            )
    email.send()

def studentDetails(request, pk):
    if StudentDetail.objects.filter(USN=pk).exists():
        s_info = StudentDetail.objects.get(USN=pk)
    else :
        s_info = 0
    student = Student.objects.get(USN=pk)
    if request.method == 'POST':
        message = request.POST['email-text']
        sendFillMail(request, message, 'Sudeep' ,student.email)
        return redirect('faculty:dashboard')
    courses = Sem.objects.filter(sem=student.current_sem, USN=pk)
    if courses.exists():
        cour = True
        marks = courses[0].CIE == None
    else:
        cour = False
        marks = False
    fastrack = Fastrack.objects.filter(USN=pk, is_active=True)
    length = fastrack.count()
    context = {'s_info': s_info, 'courses': courses, 'fasttrack': fastrack, 'fast_count': length, 'email': student.email, 'usn': student.USN, 'marks': marks, 'cour': cour}
    return render(request, 'faculty_dashboard_proctor/student_details.html', context)

def approve(request, pk):
    s_info = StudentDetail.objects.get(USN=pk)
    s_info.isApproved = True
    s_info.save()
    return redirect('faculty:student-details', pk=pk)

def courseApprove(request, pk, course_id):
    course = Sem.objects.get(USN=pk, courseCode=course_id)
    course.is_approved = True
    course.save()
    return redirect('faculty:student-details', pk=pk)

def courseReject(request, emails):
    student=Student.objects.get(email=emails)
    message = 'Looks like there is a mistake in your registered courses, check out the unapproved courses and update it'
    faculty = Faculty.objects.get(email=request.user.email)
    name = faculty.name
    template = render_to_string('faculty_dashboard_proctor/send_fill.html', {'message': message, 'name': name})
    email = EmailMessage(
        
                message,
                template,
                settings.EMAIL_HOST_USER,
                [emails],
                # fail_silently=False,
                
            )
    email.send()
    return redirect('faculty:student-details', pk=student.USN)

def addStudents(request):
    if request.method == "POST":
        excel_file = request.FILES['excel']
        print(excel_file)
        wb = pd.read_excel(excel_file)
        usn = []
        sem = []
        total = len(wb['USN'])
        for i in range(total):
            usn.append(wb['USN'][i])
            sem.append(wb['Sem'][i])
        faculty = Faculty.objects.get(email=request.user.email)   
        for usns, sems in zip(usn, sem):
            student = Student.objects.get(USN=usns)
            student.proctor_id = faculty
            student.current_sem = sems
            student.save()
        return redirect('faculty:dashboard')
    return render(request, 'faculty_dashboard_proctor/add_students.html')

def sendCourse(request):
    if request.method == "POST":
        faculty = Faculty.objects.get(email=request.user.email)
        students = Student.objects.filter(proctor_id=faculty , current_sem=int(request.POST['sems'])-1)
        emails= []
        for stud in students:
            emails.append(stud.email)
            req = courseRequest()
            req.faculty = faculty
            req.sem = int(request.POST['sems'])
            req.no_subjects = request.POST['subjects']
            req.student_usn = stud.USN
            req.save()
            stud.current_sem = int(request.POST['sems'])
            stud.save()
            courses = Sem.objects.filter(USN=stud.USN, sem=stud.current_sem-1, is_active=True)
            for course in courses:
                course.is_active = False
                course.save()
        message = "Fill the course registration form as soon as possible"
        name = faculty.name
        template = render_to_string('faculty_dashboard_proctor/send_fill.html', {'message': message, 'name': name})
        email = EmailMessage(
                message,
                template,
                settings.EMAIL_HOST_USER,
                emails,
            )
        email.send()
        return redirect('faculty:dashboard')
    return render(request, 'faculty_dashboard_proctor/course_register.html')

def sendAlertMail(request, emails):
    student=Student.objects.get(email=emails)
    message = 'Looks like you have not filled the course registration. Please fill ASAP'
    faculty = Faculty.objects.get(email=request.user.email)
    name = faculty.name
    template = render_to_string('faculty_dashboard_proctor/send_fill.html', {'message': message, 'name': name})
    email = EmailMessage(
        
                message,
                template,
                settings.EMAIL_HOST_USER,
                [emails],
                # fail_silently=False,
                
            )
    email.send()
    return redirect('faculty:dashboard')