"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")),
    path("livechat/", include("discussion_forum.chats.urls")),
    path("threads/", include("discussion_forum.threads.urls")),
    path("inbox/", include("discussion_forum.notis.urls")),
    path("direct_message/", include("discussion_forum.direct_messages.urls")),
    path("", include("discussion_forum.mainpage.urls")),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
