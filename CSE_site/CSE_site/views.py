from django.shortcuts import render

# Create your views here.
def landing_page(req):
    username = req.user.email.split('@')[0]
    return render(req, 'landing_page.html', {"username": username})