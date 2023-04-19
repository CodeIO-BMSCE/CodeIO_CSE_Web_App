from django.shortcuts import render, redirect
from .models import Notification
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.


def ShowNotifications(request):
    user = request.user
    # notifications = Notification.objects.filter(reciever=user).order_by("-date")
    # context= {
    #     "notifications": notifications,
    # }
    #TODO paginator might have error
    p = Paginator(Notification.objects.filter(reciever=user).order_by("-date"), 25) #TODO changable
    page = request.GET.get("page")
    page_of_notis = p.get_page(page)
    context= {
        "notifications": page_of_notis,
    }
    return render(request, "show_notifications.html", context)


@login_required(login_url="login")
def DeleteNotifications(request, noti_id):
    user = request.user
    Notification.objects.filter(id=noti_id, reciever=user).delete()
    return redirect("show_notifications")


def CountNotifications(request):
    count = None
    if request.user.is_authenticated:
        count = Notification.objects.filter(reciever=request.user, is_seen=False).count()
    return { "count_notifications":count }
    