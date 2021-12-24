from django.db import models
from django.contrib.auth.models import AbstractUser
from account.manager import UserManager
from account.validators import only_int


# class Person(AbstractUser):
#     username = None
#     first_name = None
#     last_name = None
#     name = models.CharField(max_length=50, null=True, blank=True)
#     email = models.EmailField(unique=True)
#     phone_no = models.CharField(max_length=10, unique=True, null=True, blank=False, validators=[only_int])
#     address = models.TextField(null=True, blank=False)
#
#     objects = UserManager()
#
#     modified_date = models.DateTimeField(auto_now_add=False, auto_now=True)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#
#     class Meta:
#         verbose_name = 'person'

class Person(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(unique=True)
    phone_no = models.CharField(max_length=10, unique=True, null=True, blank=False, validators=[only_int])
    address = models.TextField(null=True, blank=False)
    modified_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return self.email


class Employee(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    department = models.CharField(max_length=30, null=True, blank=False)
    role = models.CharField(max_length=30, null=True, blank=False)
    line_manager = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='line_manager')
    modified_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True, auto_now=False)

    def __str__(self):
        return str(self.person)

