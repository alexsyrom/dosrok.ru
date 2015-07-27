from django.shortcuts import render
from django.views import generic
from .models import Problem, Student

class Index(generic.ListView):
   model = Problem
   template_name = 'main/index.html'
   context_object_name = 'problem_list'
   def get_context_data(self, *args, **kwargs):
       context = super(Index, self).get_context_data(*args, **kwargs)
       context['student_list'] = Student.objects.all()
       return context
