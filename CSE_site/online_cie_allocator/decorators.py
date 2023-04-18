from django.shortcuts import redirect, HttpResponse
from django.urls import reverse

# currently works only if a user belongs to at most one group, TODO: make it general
def allowed_users(allowed_roles=[]):
    def decorator(in_func):
        def wrapper_func(req, *args, **kwargs):
            group = None
            if req.user.groups.exists():
                group = req.user.groups.all()[0].name

            if group in allowed_roles:
                return in_func(req, *args, **kwargs)
            else:
                return HttpResponse("You are not allowed to view this page!")
        return wrapper_func
    return decorator