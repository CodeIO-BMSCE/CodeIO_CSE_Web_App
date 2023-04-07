from django.contrib import admin
# from .models import User
<<<<<<< HEAD
from .models import Student, Faculty,Office
=======
from .models import Student, Faculty
>>>>>>> main

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

<<<<<<< HEAD
class OfficeAdmin(admin.ModelAdmin):
    list_display = ('name','email')
    search_fields = ('name','email', 'location')

=======
>>>>>>> main
    # def has_add_permission(self, _):
    #     return False

## uncomment the below line to view full User table in admin page
# admin.site.register(User,UserAdmin)
admin.site.register(Student, StudentAdmin)
<<<<<<< HEAD
admin.site.register(Faculty, FacultyAdmin)
admin.site.register(Office, OfficeAdmin)
=======
admin.site.register(Faculty, FacultyAdmin)
>>>>>>> main
