# -*- coding: utf-8 -*- 

from django.db import models
import decimal
from django.utils import timezone
from .usermodels import AbstractUser
from django.db.models.signals import m2m_changed

class MyUser(AbstractUser):
    pass

class Subject(models.Model):
    title = models.CharField("Название", max_length=200)
    is_opened = models.BooleanField('Конкурс открыт', default=True)
    end_date = models.DateField("Дата окончания конкурса", blank=True, null=True)
    rules = models.TextField('Правила конкурса', default='', blank=True)
    exam_date = models.DateField("Дата проведения досрочного экзамена", blank=True, null=True)
    place = models.CharField("Место проведения досрочного экзамена", default='', max_length=100, blank=True)
    program =models.FileField("Экзаменационная программа", blank=True, null=True) 
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Предмет'
        verbose_name_plural = 'Предметы'


class Example(models.Model):
    title = models.CharField("Название", max_length=200)
    statement = models.FileField("Условие")
    comment = models.FileField("Комментарий", blank=True, null=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Пример'
        verbose_name_plural = 'Примеры'


problem_shift = 100000

class Problem(models.Model):
    title = models.CharField("Название", max_length=200)
    is_title_hidden = models.BooleanField('Скрыто', default = False)

    statement = models.FileField("Условие")
    is_statement_hidden = models.BooleanField('Скрыто', default = False)

    number = models.PositiveIntegerField("Номер")
    is_number_hidden = models.BooleanField('Скрыто', default = False)

    KID = models.CharField("ID", max_length=10, editable=False)
    #is_KID_hidden = models.BooleanField('Скрыто', default = False)
    # always hidden

    OPENED = 'OPENED'
    CLOSED = 'CLOSED'
    STATE_CHOICES = (
        (OPENED, 'Конкурс открыт'),
        (CLOSED, 'Конкурс закрыт'),
    )
    #state = models.CharField("Конкурсное состояние", max_length=10, choices=STATE_CHOICES)
    state = models.BooleanField("Конкурс открыт", default=True)
    is_state_hidden = models.BooleanField('Скрыто', default = False)

    end_date = models.DateField("Дата окончания конкурса", blank=True, null=True)
    is_end_date_hidden = models.BooleanField('Скрыто', default = False)

    student_num = models.PositiveIntegerField("Число студентов, решивших задачу", default=0, editable=False)
    is_student_num_hidden = models.BooleanField('Скрыто', default = False)

    rating = models.DecimalField("Рейтинг", max_digits=9, decimal_places=8, default=decimal.Decimal('0.0'), editable=False) #MySql can't in infinity
    is_rating_hidden = models.BooleanField('Скрыто', default = False)

    solution = models.FileField("Решение", blank=True, null=True)
    is_solution_hidden = models.BooleanField('Скрыто', default = False)

    comment = models.FileField("Комментарий", blank=True, null=True)
    is_comment_hidden = models.BooleanField('Скрыто', default = False)
    
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if not self.id:
            self.KID = "P{0}".format(problem_shift + self.number)
        if self.student_num > 0:
            self.rating = decimal.Decimal(1) / decimal.Decimal(self.student_num)
        else:
            self.rating = 0
        return super(Problem, self).save(*args, **kwargs)
    def is_opened(self):
        if self.end_date:
            if self.end_date > timezone.now():
                self.state = False
                self.save()
        return self.state
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'



class Student(models.Model):
    lastname = models.CharField('Фамилия', max_length=50, blank=True)
    firstname = models.CharField('Имя', max_length=50, blank=True)
    group = models.CharField('Группа', max_length=6, blank=True)
    solved_problems = models.ManyToManyField(Problem, verbose_name='Решённые задачи', blank=True)
    KID = models.CharField("ID", max_length=255, blank=True, editable=False, unique=True)
    rating = models.DecimalField('Рейтинг', max_digits=11, decimal_places=8, default=decimal.Decimal('0.0'), editable=False)
    is_allowed = models.BooleanField('Допуск', default = False)
    nec_conditions = models.BooleanField('Необходимые условия', default = False)
    recommendation = models.BooleanField('Рекомендация преподавателя', default = False)
    PRS = models.PositiveIntegerField("БРС", default=0)
    test_mark = models.PositiveIntegerField("Семестровая", default=0)
    def __str__(self):
        return "{0} {1} {2}".format(self.lastname, self.firstname, self.group)
    def get_problem_list(self):
        return ', '.join([str(problem.number) for problem in self.solved_problems.all().only('number')])
    def save(self, *args, **kwargs):
        if not self.id:
            self.KID = "{0} {1} {2}".format(self.lastname, self.firstname, self.group)
        return super(Student, self).save(*args, **kwargs)
    class Meta:
        unique_together = (('lastname', 'firstname', 'group', ), )
        verbose_name = 'Участник'
        verbose_name_plural = 'Участники'

def update_rating(sender, instance, action, reverse, model, pk_set, **kwargs):
    """
    I'm really sorry, but Django don't send remove signal. It even doesn't do remove opearions, it clears all and after it adds.
    So we need to do this fucking shit in 'Django way'
    """
    if action == 'post_add' or action == 'post_clear': #if somebody removes all problems, there will be no add signal
        if action == 'post_add':
            problems = set(instance.solved_problems.all())
        else:
            problems = instance.old_solved_problems
        for problem in problems:
            problem.student_num = problem.student_set.count()
            problem.save()
        problems_pk_set = [problem.pk for problem in problems]
        students = set(Student.objects.filter(solved_problems__pk__in=problems_pk_set)) | set([instance,])
        for student in students:
            student.rating = sum([problem.rating for problem in student.solved_problems.only('rating')]) 
            student.save()
    elif action == 'pre_clear':
        instance.old_solved_problems = set(instance.solved_problems.all())

m2m_changed.connect(update_rating, sender=Student.solved_problems.through)
