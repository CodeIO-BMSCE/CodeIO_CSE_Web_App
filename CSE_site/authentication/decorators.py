from django.shortcuts import redirect
from django.urls import reverse

def already_logged_in(url='landing_page'):
    def decorator(in_func):
        def wrapper_func(req, *args, **kwargs):
            if req.user.is_authenticated == True:
                return redirect(reverse(url))
            else:
                return in_func(req, *args, **kwargs)
        return wrapper_func
    return decorator