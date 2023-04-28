from django.shortcuts import render

# Create your views here.
def landing_page(req):
    username = req.user.email.split('@')[0]
    is_user_office = len(req.user.groups.filter(name="Office")) != 0
    return render(req, 'landing_page.html', { "username": username, "is_user_office": is_user_office })