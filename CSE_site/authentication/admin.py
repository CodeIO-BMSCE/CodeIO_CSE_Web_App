from django.contrib import admin
# from .models import User
from .models import Student, Faculty

class UserAdmin(admin.ModelAdmin):
    list_display = ('name','email')
    search_fields = ('name','email')

    # def has_delete_permission(self, request, obj=None):
    #     return False

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','email', 'usn')
    search_fields = ('name','email', 'usn')

    # def has_add_permission(self, _):
    #     return False

class FacultyAdmin(admin.ModelAdmin):
    list_display = ('name','email')
    search_fields = ('name','email', 'designation')

    # def has_add_permission(self, _):
    #     return False

## uncomment the below line to view full User table in admin page
# admin.site.register(User,UserAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Faculty, FacultyAdmin)