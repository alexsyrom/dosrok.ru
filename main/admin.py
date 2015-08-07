from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Problem, Student, MyUser, Main, Example

class ProblemAdmin(admin.ModelAdmin):
    readonly_fields = ('KID', 'student_num', 'rating',)

class StudentAdmin(admin.ModelAdmin):
    readonly_fields = ('KID', 'rating',)

admin.site.register(Problem, ProblemAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(MyUser, UserAdmin)
admin.site.register(Main)
admin.site.register(Example)


