from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form =CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = [
        "email",
        "username",
        "USN",
        "is_staff",
    ]
    fieldsets = UserAdmin.fieldsets + ((None, {"fields" : ("USN",)}),)

admin.site.register(CustomUser, CustomUserAdmin)
