"""imported modules"""
from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Company(models.Model):
    """company model"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    company_employees = models.IntegerField(default = 10)

    CHOICES = [
        ('software company', 'Software Company'),
        ('media agency', 'Media Agency'),
        ('trading agency', 'Trading Agency'),
    ]
    company_type = models.CharField(max_length=255, choices=CHOICES, default = 'Software Company')
    country = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.company_name}"

class Client(models.Model):
    """client model"""
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, related_name = 'clients')
    client_name = models.CharField(max_length=255)
    client_contact = PhoneNumberField(null=True)

    CHOICES = [
        ('active', 'Active'),
        ('deactive', 'Deactive'),
    ]
    client_status = models.CharField(max_length=255, choices=CHOICES, default = 'Active')

    def __str__(self):
        return f"{self.client_name}"

class Project(models.Model):
    """project model"""
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name = 'projects')
    project_name = models.CharField(max_length=255)
    project_created = models.DateTimeField(auto_now_add=True, null=True)
    project_deadline = models.DateField()

    def __str__(self):
        return f"{self.project_name}"

class Member(models.Model):
    """member model"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name = 'members')
    member_name = models.CharField(max_length=255)
    member_email = models.EmailField(max_length=50)
    CHOICES = [
        ('manager', 'Manager'),
        ('employee', 'Employee'),
    ]
    member_role = models.CharField(max_length=255, choices=CHOICES, default = 'Employee')

    def __str__(self):
        return f"{self.member_name}"

class RegisterHours(models.Model):
    """register hours model"""
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    date = models.DateField(default = datetime.today())
    time_spent = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.project}"
