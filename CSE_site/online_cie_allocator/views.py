from django.shortcuts import render, HttpResponse

def office_view(req):
    return render(req, "cie_allocator_office.html", {})

def student_view(req):
    return HttpResponse("This is CIE Allocator Home Page")