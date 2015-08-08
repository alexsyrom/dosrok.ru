from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django import forms

from .models import Problem, Student, MyUser, Subject, Example

class ProblemAdmin(admin.ModelAdmin):
    readonly_fields = ('KID', 'student_num', 'rating',)
    fields = (
              ('is_title_hidden', 'title', ),
              ('is_statement_hidden', 'statement', ),
              ('is_number_hidden', 'number', ),
              ('is_state_hidden', 'state', ),
              ('is_end_date_hidden', 'end_date', ),
              ('is_solution_hidden', 'solution', ),
              ('is_comment_hidden', 'comment', ),
              ('is_student_num_hidden', 'student_num', ),
              ('is_rating_hidden', 'rating', ),
              ('KID', ),
              )


class StudentAdmin(admin.ModelAdmin):
    readonly_fields = ('KID', 'rating',)
    filter_horizontal = ('solved_problems',)

admin.site.register(Problem, ProblemAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(MyUser, UserAdmin)
admin.site.register(Subject)
admin.site.register(Example)


