from django.shortcuts import redirect, HttpResponse
from django.urls import reverse

def allowed_users(allowed_roles=[]):
    def decorator(in_func):
        def wrapper_func(req, *args, **kwargs):
            group = None
            if req.user.groups.exists():
                for user_group in req.user.groups.all():
                    if user_group.name in allowed_roles:
                        return in_func(req, *args, **kwargs)
                
            return HttpResponse("You are not allowed to view this page!")
        return wrapper_func
    return decorator