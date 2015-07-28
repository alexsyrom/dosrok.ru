from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Problem, Student, MyUser

admin.site.register(Problem)
admin.site.register(Student)
admin.site.register(MyUser, UserAdmin)


