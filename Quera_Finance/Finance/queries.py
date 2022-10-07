from django.db.models import F, Q, Sum, Count, Case, When
from .models import *


def query_0():
    q = Employee.objects.all()
    return q


def query_1():
    return Payslip.objects.filter(payment=None).aggregate(
    total_dept=Sum('base')+Sum('tax')+Sum('insurance')+Sum('overtime'))


def query_2(x):
    return Payslip.objects.filter(salary__overtime__gte=x).aggregate(
    total_overtime=Sum('overtime'))


def query_3():
    return Payment.objects.aggregate(total=Sum('amount'))


def query_4(x):
    return EmployeeProjectRelation.objects.filter(employee=x).aggregate(total_hours=Sum('hours'))


def query_5(x):
    salary = Salary.objects.annotate(total_amount=Sum('payslip__payment__amount')).filter(total_amount__gte=x)
    return Employee.objects.filter(salary__in=salary)


def query_6():
    return Employee.objects.annotate(total_hours=Sum(
    'employeeprojectrelation__hours')
    ).order_by('-total_hours', 'account__username').first()


def query_7():
    return Department.objects.annotate(total=Sum(
    'project__employees__salary__payslip__payment__amount')
    ).order_by('-total', 'name').first()


def query_8():
    return Department.objects.filter(project__estimated_end_time__gte=F(
    'project__end_time')
    ).annotate(early_delivery_count=Count('project')).order_by('-early_delivery_count', 'name').first()


def query_9(x):
    return Employee.objects.annotate(late_count=Count(
    Case(
        When(attendance__in_time__lte=x, then=1),
    ))).order_by('-late_count', 'account__username').first()


def query_10():
    projects = Project.objects.all()
    return {'total': Employee.objects.exclude(project__in=projects).count()}
