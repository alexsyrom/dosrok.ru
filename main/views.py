from django.shortcuts import render
from django.views import generic
from .models import Problem, Student, Example, Subject

class Index(generic.ListView):
    model = Problem
    template_name = 'main/index.html'
    context_object_name = 'problem_list'
    def get_context_data(self, *args, **kwargs):
        context = super(Index, self).get_context_data(*args, **kwargs)
        context['student_list'] = Student.objects.all().order_by('-rating')
        context['allowed_student_list'] = Student.objects.all().filter(is_allowed=True)
        context['example_list'] = Example.objects.all()
        context['subject'] = Subject.objects.all().order_by('id')[0]
        return context
    def get_queryset(self):
        return Problem.objects.all().order_by('number')
