from django.db import models
import decimal
from django.utils import timezone

problem_shift = 100000

class Problem(models.Model):
    title = models.CharField("Название", max_length=200)
    statement = models.FileField("Условие")
    number = models.PositiveIntegerField("Номер")
    KID = models.CharField("ID", max_length=10, blank=True)
    OPENED = 'OPENED'
    CLOSED = 'CLOSED'
    STATE_CHOICES = (
        (OPENED, 'Конкурс открыт'),
        (CLOSED, 'Конкурс закрыт'),
    )
    state = models.CharField("Конкурсное состояние", max_length=10, choices=STATE_CHOICES)
    end_date = models.DateField("Дата окончания конкурса", blank=True, null=True)
    student_num = models.PositiveIntegerField("Число студентов, решивших задачу", default=0)
    rating = models.DecimalField("Рейтинг", max_digits=9, decimal_places=8, default=decimal.Decimal('Infinity'))
    solution = models.FileField("Решение", blank=True, null=True)
    comment = models.FileField("Комментарий", blank=True, null=True)
    
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if not self.id:
            self.KID = "P{0}".format(problem_shift + self.number)
        if self.student_num > 0:
            self.rating = decimal.Decimal(1) / decimal.Decimal(self.student_num)
        return super(Problem, self).save(*args, **kwargs)
    def is_opened(self):
        if self.end_date:
            if self.end_date > timezone.now():
                self.state = Problem.CLOSED
                self.save()
        if self.state == Problem.OPENED:
            return True
        else:
            return False


class Student(models.Model):
    lastname = models.CharField('Фамилия', max_length = 50, blank=True)
    firstname = models.CharField('Имя', max_length = 50, blank=True)
    group = models.PositiveIntegerField('Группа', blank=True)
    solved_problems = models.ManyToManyField(Problem)
    KID = models.CharField("ID", max_length=10, blank=True, default=0)
    rating = models.DecimalField("Рейтинг", max_digits=11, decimal_places=8, default=decimal.Decimal('Infinity'))
    is_allowed = models.BooleanField('Допуск', default = False)
    nec_conditions = models.BooleanField('Необходимые условия', default = False)
    recommendation = models.BooleanField('Рекомендация преподавателя', default = False)
    PRS = models.PositiveIntegerField("БРС", default=0)
    test_mark = models.PositiveIntegerField("Семестровая", default=0)
    def __str__(self):
        return "{0} {1} {2}".format(lastname, firstname, group)

