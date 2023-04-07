from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
# from .resources import StudentResource
# from tablib import Dataset
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
    section = Student.objects.filter(email=studentemail).values('section').first()['section']
    courses = Course.objects.filter(className = section).values('courses').first()['courses'].strip("][").replace("'","").split(",")
    facultyHandles = Course.objects.filter(className = section).values('facultyHandles').first()['facultyHandles'].strip("][").replace("'","").split(",")
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
        current_user = request.user
        faculty = current_user.email
        newcourse=FacultyCourse(courseTitle=courseTitle , courseCode=courseCode , semester=semester , section=section , faculty=faculty)

        if request.FILES.get('classfile'):
            # student_resource = StudentResource()
            dataset = Dataset()
            new_students = request.FILES.get('classfile')
            if not new_students.name.endswith('xlsx'):
                messages.info(request , 'Use the excel file only')
                return render(request , 'facultyCourses.html')
            
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

def facultyAttendance(request):
    if request.method == 'POST' and  request.FILES.get('classfile'):
        # student_resource = StudentResource()
        dataset = Dataset()
        new_students = request.FILES.get('classfile')
        if not new_students.name.endswith('xlsx'):
            messages.info(request , 'Use the excel file only')
            return render(request , 'facultyCourses.html')
        
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

def Logout(request):
    return redirect('auth_logout')
