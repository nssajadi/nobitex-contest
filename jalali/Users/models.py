import math
import jdatetime
from django.db import models
from django_jalali.db import models as jmodels


GENDER_CHOICES = (
    ('F', 'Female'),
    ('M', 'Male')
)

class CustomUser(models.Model):
    username = models.CharField(max_length=256, null=True)
    full_name = models.CharField(max_length=256, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, null=True)
    national_code = models.CharField(max_length=10, null=True)
    birthday_date = jmodels.jDateField(null=True)
    ceremony_datetime = jmodels.jDateTimeField(null=True)
    country = models.CharField(max_length=4, editable=False, default='Iran')

    def get_first_and_last_name(self):
        splitted_name = self.full_name.split(' ')
        return {'first_name': splitted_name[0], 'last_name': splitted_name[1]}

    def get_age(self):
        today = jdatetime.date.today()
        return ((today-self.birthday_date).days//365)

    def is_birthday(self):
        today = jdatetime.date.today()
        return (today.month == self.birthday_date.month and today.day == self.birthday_date.day)
