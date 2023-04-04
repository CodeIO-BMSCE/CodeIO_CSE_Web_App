from django.shortcuts import render

# Create your views here.
def landing_page(req):
    return render(req, 'landing_page.html', {})