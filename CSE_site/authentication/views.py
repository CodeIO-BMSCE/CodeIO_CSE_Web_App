from .funtions import *
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.urls import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import Group
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.hashers import make_password
from student_dashboard_proctor.models import Student as student
from faculty_dashboard_proctor.models import Faculty as facs
from Attendence_Management.models import *

from .models import User, Student, Faculty
from .decorators import already_logged_in
from .utils import token_generator

def send_activation_email(user, request):
    current_site = get_current_site(request)
    email_subject = 'Verify your email'
    email_body = render_to_string('auth/activate.html', {
        'user': user,
        'domain': current_site,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': token_generator.make_token(user)
    })

    send_mail(email_subject, email_body, settings.EMAIL_HOST_USER, [user.email])

@already_logged_in(url="landing_page")
def auth_home(req):
    context = {
        "flink_title": "Login",
        "flink": "auth_login_home",
        "slink_title": "Register",
        "slink": "auth_register_home",

    }

    return render(req, "auth_home.html", context)

@already_logged_in(url="landing_page")
def register_home(req):
    context = {
        "flink_title": "Student Register",
        "flink": "auth_register_student",
        "slink_title": "Faculty Register",
        "slink": "auth_register_faculty",
    }
    return render(req, "auth_home.html", context)

@already_logged_in(url="landing_page")
def login_home(req):
    context = {
        "flink_title": "Student Login",
        "flink": "auth_login_student",
        "slink_title": "Faculty Login",
        "slink": "auth_login_faculty",
        "olink_title": "Office Login",
        "olink": "auth_login_office",
    }
    return render(req, "auth_home.html", context)

@already_logged_in(url="landing_page")
def register_student(req):
    context = {}

    if req.method == 'POST':
        name = req.POST.get('name')
        usn = req.POST.get('usn')
        email = req.POST.get('email')
        password = req.POST.get('password')
        confirm_password = req.POST.get('confirm_password')

        if not validateEmailStudent(email):
            messages.add_message(req, messages.ERROR,'Enter your BMSCE Mail')
            return render(req, 'register_student.html', context, status=409)

        # if not validatePassword(password):
        #     messages.add_message(req, messages.ERROR,' Password must contain minimum 8 and maximum 16 characters, at least one uppercase letter, one lowercase letter, one number and one special character')
        #     return render(req, 'register_student.html', context,  status=409)

        if password != confirm_password:
            messages.add_message(req, messages.ERROR,'Password mismatch')
            return render(req, 'register_student.html', context, status=409)

        if Student.objects.filter(email=email).exists():
            messages.add_message(req, messages.ERROR,'You are already Registered, Login!')
            return redirect(reverse('auth_register_student'))

        try:
            group = Group.objects.get(name="Student")
        except ObjectDoesNotExist:
            group = Group.objects.create(name="Student")  

        stud = Student.objects.create_user(email=email, password=password)
        stud.name = name
        stud.usn = usn
        stud.groups.add(group)
        stud.save()
        details=student()
        details.name=name
        details.USN=usn
        details.email=email
        details.save()
        messages.add_message(req, messages.SUCCESS, 'We sent you an email to verify your account')

        send_activation_email(stud, req)
        return redirect(reverse('auth_login_student'))

    return render(req, "register_student.html", context)


@already_logged_in(url="landing_page")
def register_faculty(req):
    context = {}
    if req.method == 'POST':
        name = req.POST.get('name')
        email = req.POST.get('email')
        password = req.POST.get('password')
        confirm_password = req.POST.get('confirm_password')

        if not validateEmailFaculty(email):
            messages.add_message(req, messages.ERROR,'Enter your BMSCE Mail')
            return render(req, 'register_faculty.html', context, status=409)
        
        if not validatePassword(password):
            messages.add_message(req, messages.ERROR,' Password must contain minimum 8 and maximum 16 characters, at least one uppercase letter, one lowercase letter, one number and one special character')
            return render(req, 'register_faculty.html', context,  status=409)

        if password != confirm_password:
            messages.add_message(req, messages.ERROR,'Password mismatch')
            return render(req, 'register_faculty.html', context, status=409)

        if Faculty.objects.filter(email=email).exists():
            messages.add_message(req, messages.ERROR,'You are already Registered, Login!')
            return redirect(reverse('auth_register_faculty'))

        try:
            group = Group.objects.get(name="Faculty")
        except ObjectDoesNotExist:
            group = Group.objects.create(name="Faculty")  

        fac = Faculty.objects.create_user(email=email, password=password)
        fac.name = name
        fac.groups.add(group)
        fac.save()
        details=facs()
        details.name=name
        details.email=email
        details.save()
        messages.add_message(req, messages.SUCCESS, 'We sent you an email to verify your account')

        send_activation_email(fac, req)
        return redirect(reverse('auth_login_faculty'))

    return render(req, "register_faculty.html", context)

@already_logged_in(url="landing_page")
def login_student(req):
    context = {}

    if req.method == "POST":
        email = req.POST.get('email')
        password = req.POST.get('password')

        user = authenticate(req, email=email, password=password)

        if not user:
                messages.add_message(req,messages.ERROR, "Invalid credentials, try again")
                return render(req, 'login_student.html', context,  status=409)
        
        if not user.is_email_verified:
                messages.add_message(req, messages.ERROR, "Student Email Not Verified! Check your Inbox")
                return render(req, 'login_student.html', context,  status=409)
        
        if not user.groups.filter(name="Student"):
            messages.add_message(req,messages.ERROR,"Invalid Student credentials, try again")
            return render(req, 'login_student.html', context,  status=409)

        login(req, user)
        return redirect(reverse("landing_page"))

    return render(req, "login_student.html", {})

@already_logged_in(url="landing_page")
def login_faculty(req):
    context = {}

    print(req.user)

    if req.method == "POST":
        email = req.POST.get('email')
        password = req.POST.get('password')

        user = authenticate(req, email=email, password=password)

        if not user:
                messages.add_message(req,messages.ERROR, "Invalid credentials, try again")
                return render(req, 'login_faculty.html', context,  status=409)
        
        if not user.is_email_verified:
                messages.add_message(req, messages.ERROR, "Faculty Email Not Verified! Check your Inbox")
                return render(req, 'login_faculty.html', context,  status=409)
        
        if not user.groups.filter(name="Faculty"):
            messages.add_message(req,messages.ERROR,"Invalid Faculty credentials, try again")
            return render(req, 'login_faculty.html', context,  status=409)

        login(req, user)
        return redirect(reverse("landing_page"))

    return render(req, "login_faculty.html", {})

@already_logged_in(url="landing_page")
def login_office(req):
    context = {}

    print(req.user)

    if req.method == "POST":
        email = req.POST.get('email')
        password = req.POST.get('password')

        user = authenticate(req, email=email, password=password)

        if not user:
                messages.add_message(req,messages.ERROR, "Invalid credentials, try again")
                return render(req, 'login_office.html', context,  status=409)
        
        if not user.is_email_verified or not user.groups.filter(name="Office"):
                messages.add_message(req, messages.ERROR, "Use the Office Email ID")
                return render(req, 'login_office.html', context,  status=409)

        login(req, user)
        return redirect(reverse("landing_page"))

    return render(req, "login_office.html", {})


def forgot_password(req):
    if req.method == "POST":
        email = req.POST['email']
        try:
            user=User.objects.get(email=email)
        except User.DoesNotExist:
            user = None
        if User.objects.filter(email=email).exists():
            current_site = get_current_site(req)
            email_subject = 'Reset your password'
            email_body = render_to_string('reset_password/reset_mail.html', {
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': token_generator.make_token(user)
            })
            send_mail(email_subject, email_body,settings.EMAIL_HOST_USER,[email])
            #messages.add_message(request, messages.SUCCESS,'Mail has been sent to your Registered Email address {}'.format(email))
            return redirect(reverse('auth_reset_password_done'))
        else:
            messages.error(req, 'Email address does not exist')
    
    return render(req, 'reset_password/forgot_password.html')

def reset_password(req, uidb64, token):
    try:
        userpk = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=userpk)
        if user and token_generator.check_token(user, token):
            if req.method == "POST":
                password1 = req.POST['new_password']
                password2 = req.POST['new_password2']
                if password1 == password2:
                    user.password = make_password(password1)
                    user.save()
                    #messages.success(request,'Password has been reset successfully')
                    return redirect(reverse('auth_reset_password_complete'))
                else:
                    return HttpResponse('Two Password did not match')
                
        else:
            return HttpResponse('Wrong URL')
    except Exception as e:
        return HttpResponse('Wrong URL')
    return render(req, 'reset_password/reset_password.html')

def logout_user(req):
    logout(req)
    messages.add_message(req, messages.SUCCESS,'Successfully logged out')
    return redirect(reverse('auth_home'))

def verify_email(req, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except Exception as e:
        print(e)
        user = None

    if user and token_generator.check_token(user, token):
        user.is_email_verified = True
        user.save()

        messages.add_message(req, messages.SUCCESS,
                             'Email verified, you can now login')
        return redirect(reverse('auth_login_student'))

    return HttpResponse("Something wrong with your Link! or the email is already verified")

def proctor_management(request):
    if(request.user.groups.filter(name="Student").exists()):
        students=student.objects.get(email=request.user.email)
        if(students.proctor_id):
            return redirect( 'student:dashboard', pk=students.USN)
        else:
            #edit the message
            return redirect('student:no_proctor')
    elif(request.user.groups.filter(name="Faculty").exists()):
        return redirect('faculty:dashboard')
    else:
        return redirect('office:dashboard')

    
def atttendence_management(request):
    if(request.user.groups.filter(name="Student").exists()):
        return redirect('attendance:studentdashboard')
    elif(request.user.groups.filter(name="Faculty").exists()):
        # return render(request , "Attendence_Management/facultyCourses.html")
        return redirect('attendance:facultyCourses')
    else:
        return redirect(reverse('attendance:auth_home'))
