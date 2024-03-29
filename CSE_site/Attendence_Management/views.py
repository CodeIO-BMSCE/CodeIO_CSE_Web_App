from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from .resources import StudentResource
from tablib import Dataset
from .models import *
from django.urls import reverse

# Create your views here.
# def home(request ,*args , **kwargs):
#     if request.method == 'POST':
#         attendance = request.POST.getlist('attendance')
#         section = request.GET.get('section')
#         courseTitle = request.GET.get('courseTitle')
#         entry = Attendance(attendance=attendance , section = section , courseTitle = courseTitle)
#         entry.save()
#         print('data saved successfully')
#     return render(request , "home.html",{})

# def SignUp(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         email = request.POST['email']
#         fullname = request.POST['fullname']
#         password1 = request.POST['password1']
#         password2 = request.POST['password2']
#         usertype = request.POST['usertype']
#         if not email.endswith("@bmsce.ac.in"):
#             messages.info(request , "Use college email id only")
#             return redirect('signup')
#         if password1 == password2:
#             if User.objects.filter(email=email).exists():
#                 messages.info("Email is already taken")
#                 return redirect('signup')
#             elif User.objects.filter(username=username).exists():
#                 messages.info("Username is already taken")
#                 return redirect('signup')
#             else:
#                 user = User.objects.create_user(email=email , password=password1 , username=username ,fullname=fullname,usertype=usertype)
#                 user.save()
#                 messages.info(request , "You're registered successfully")
#                 return redirect('login')
#         else:
#             messages.info(request ,"Your passwords didn't match")
#             return redirect('signup')
#     return render(request , "SignUp.html")
	 

# def Login(request):
#     if request.method == 'POST':
#         email = request.POST['email']
#         password = request.POST['password']
#         user = authenticate(email=email , password=password)
#         if user is not None:
#             login(request, user)
#             if user.usertype == 'Student':
#                 return redirect('studentdashboard')
#             if user.usertype == 'Faculty':
#                 return redirect('facultyCourses')
#         else:
#             messages.info(request,'Account Does not exist , please Sign Up')
#             return redirect('login')
#     return render(request, 'login.html')


def StudentDashboard(request):
    studentemail = request.user.email
    section = Student.objects.filter(email=studentemail).values('section').first()['section'] if Student.objects.filter(email=studentemail).exists() else None
    if section is None:
        messages.info(request,"Wait until data gets added")
        return render(request, '../templates/Attendence_Management/studentdashboard.html')
    courses = Course.objects.filter(className = section).values('courses').first()['courses'].strip("][").replace("'","").split(",") if Course.objects.filter(className = section) else None
    facultyHandles = Course.objects.filter(className = section).values('facultyHandles').first()['facultyHandles'].strip("][").replace("'","").split(",") if Course.objects.filter(className = section) else None
    if courses is None or facultyHandles is None:
        messages.info(request,"Wait until data gets added")
        return render(request, '../templates/Attendence_Management/studentdashboard.html')
    flist = zip(courses , facultyHandles)
    return render(request, '../templates/Attendence_Management/studentdashboard.html',{'flist':flist})

def StudentCourse(request):
    studentemail = request.user.email
    courseTitle = request.GET.get('courseTitle')
    usn = Student.objects.filter(email=studentemail).values('usn').first()['usn']
    section = Student.objects.filter(email=studentemail).values('section').first()['section']
    entries = Attendance.objects.filter(section=section , courseTitle=courseTitle)
    totalClasses = entries.count()
    entries = entries.values()
    attendedClasses = 0

    for entry in entries:
        attList = entry['attendance'].strip("][").replace("'","").split(", ")
        if usn in attList:
            attendedClasses += 1

    if attendedClasses == 0:
        messages.info(request,"You haven't attended any classes yet :(")
        return redirect(reverse('studentdashboard'))
    per = (attendedClasses/totalClasses)*100
    status = {
        'courseTitle':courseTitle ,
        'totalClasses':totalClasses,
        'attendedClasses':attendedClasses,
        'percentage': per,
        'stat':'Eligible' if per >= 85 else 'Not Eligible'
    }
    return render(request, '../templates/Attendence_Management/studentcourse.html', {'status':status})

def facultyCourses(request):
    curr=request.user
    mydata=FacultyCourse.objects.filter(faculty=curr.email)
    if request.method == 'POST' and request.POST.get('semester'):
        courseTitle = request.POST['courseTitle']
        courseCode = request.POST['courseCode']
        semester = request.POST['semester']
        section = request.POST['section']
        academicYear=request.POST['academicYear']
        current_user = request.user
        faculty = current_user.email
        newcourse=FacultyCourse(courseTitle=courseTitle , courseCode=courseCode , semester=semester , section=section , faculty=faculty,academicYear=academicYear)

        if request.FILES.get('classfile'):
            student_resource = StudentResource()
            dataset = Dataset()
            new_students = request.FILES.get('classfile')
            if not new_students.name.endswith('xlsx'):
                messages.info(request , 'Use the excel file only')
                return render(request , '../templates/Attendence_Management/facultyCourses.html')
            
            imported_data = dataset.load(new_students.read() , format='xlsx')
            for data in imported_data:
                value = Student(
                    data[0],
                    data[1],
                    data[2],
                    data[3],
                    data[4],
                )
                value.save()
        newcourse.save()
        messages.success(request , 'New Course Added Successfully')
    elif request.method == 'POST' and request.POST.get('attendance'):
        attendance = request.POST.getlist('attendance')
        section = request.GET.get('section')
        courseTitle = request.GET.get('courseTitle')
        entry = Attendance(attendance=attendance , section = section , courseTitle = courseTitle)
        entry.save()
        messages.success(request , 'Attendance Marked Successfully')
    return render(request , '../templates/Attendence_Management/facultyCourses.html',{'mydata':mydata})

def updateCourse(request, course_code,section):
    curr=request.user
    mydata=FacultyCourse.objects.filter(faculty=curr.email)
    courseinfo = FacultyCourse.objects.get(courseCode=course_code,faculty=curr.email,section=section)
    courseinfo.courseTitle = request.POST['courseTitle']
    courseinfo.courseCode = request.POST['courseCode']
    courseinfo.semester = request.POST['semester']
    courseinfo.section = request.POST['section']
    current_user = request.user
    courseinfo.faculty = current_user.email
    courseinfo.save()
    messages.success(request , 'Course details Updated Successfully')
    return redirect(reverse('facultyCourses'))

def deleteCourse(request,course_title, course_code,section):
    curr=request.user
    mydata=FacultyCourse.objects.filter(faculty=curr.email)
    coursedel = FacultyCourse.objects.get(courseTitle=course_title, courseCode=course_code,faculty=curr.email,section=section)
    coursedel.delete()
    messages.success(request , 'Course Removed Successfully')
    return redirect(reverse('facultyCourses'))

def academicyear(request,academic_year):
    curr=request.user
    mydata=FacultyCourse.objects.filter(academicYear=academic_year,faculty=curr.email)
    return redirect(reverse('facultyCourses'))


def facultyAttendance(request):
    if request.method == 'POST' and  request.FILES.get('classfile'):
        student_resource = StudentResource()
        dataset = Dataset()
        new_students = request.FILES.get('classfile')
        if not new_students.name.endswith('xlsx'):
            messages.info(request , 'Use the excel file only')
            return render(request , '../templates/Attendence_Management/facultyCourses.html')
        
        imported_data = dataset.load(new_students.read() , format='xlsx')
        for data in imported_data:
            value = Student(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
            )
            value.save()
        messages.success(request , 'Successfully added the student data')
    section=request.GET.get('section')
    courseTitle = request.GET.get('courseTitle')
    students = Student.objects.filter(section=section)
    count = students.count()
    return render(request,'../templates/Attendence_Management/facultyAttendance.html' ,{'students':students , 'count':count , 'section':section , 'courseTitle':courseTitle})

def studentList(request):
    courseTitle = request.GET.get('courseTitle')
    section = request.GET.get('section')
    action = request.GET.get('action')
    if request.method == 'POST' and action=='add':
        date = request.POST['date']
        entry = Attendance.objects.filter(date=date , section=section , courseTitle=courseTitle).values('attendance').first()['attendance'] if Attendance.objects.filter(date=date , section=section , courseTitle=courseTitle).exists() else None
        if entry is None:
            messages.info(request , f"No attendance has been recorded the day {date}")
            return redirect(reverse('facultyCourses'))
        entry = entry.strip("][").replace("'","").split(", ")
        usn = request.GET.get('usn')
        if usn in entry:
            messages.info(request , f"Already marked present for the day {date}")
            return redirect(reverse('facultyCourses'))
        entry.append(usn)
        Attendance.objects.filter(date=date , section=section , courseTitle=courseTitle).update(attendance=entry)
        messages.info(request , f"Updated successfully")
        return redirect(reverse('facultyCourses'))
    if request.method == 'POST' and action=='remove':
        date = request.POST['date']
        entry = Attendance.objects.filter(date=date , section=section , courseTitle=courseTitle).values('attendance').first()['attendance'] if Attendance.objects.filter(date=date , section=section , courseTitle=courseTitle).exists() else None
        if entry is None:
            messages.info(request , f"No attendance has been recorded the day {date}")
            return redirect(reverse('facultyCourses'))
        entry = entry.strip("][").replace("'","").split(", ")
        usn = request.GET.get('usn')
        if not usn in entry:
            messages.info(request , f"Marked absent for the day {date}")
            return redirect(reverse('facultyCourses'))
        entry.remove(usn)
        Attendance.objects.filter(date=date , section=section , courseTitle=courseTitle).update(attendance=entry)
        messages.info(request , f"Updated successfully")
        return redirect(reverse('facultyCourses'))
    students = Student.objects.filter(section=section)
    entries = Attendance.objects.filter(section=section , courseTitle=courseTitle)
    totalClasses = entries.count()
    entries = entries.values()
    usn = []
    attended = []
    percentage = []
    stat = []
    for student in students:
        attendedClasses = 0
        for entry in entries:
            attList = entry['attendance'].strip("][").replace("'","").split(", ")
            if student.usn in attList:
                attendedClasses += 1
        usn.append(student.usn)
        attended.append(attendedClasses)
        per = 0 if attendedClasses==0 else (attendedClasses/totalClasses)*100
        percentage.append(per)
        s = 'Eligible' if per >= 85 else 'Not Eligible'
        stat.append(s)
    status = zip(usn , attended  , percentage , stat)
    return render(request, '../templates/Attendence_Management/studentList.html', {'status':status , 'totalClasses':totalClasses , 'section':section , 'courseTitle':courseTitle})

def Logout(request):
    return redirect('auth_logout')
