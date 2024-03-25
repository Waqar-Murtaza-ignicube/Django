"""imported modules"""
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from .models import Client, Company, Project, Member, RegisterHours


class CreateClient(forms.ModelForm):
    """client form"""
    client_contact = PhoneNumberField()
    class Meta:
        """client form fields"""
        model = Client
        fields = ['client_name', 'client_contact', 'client_status']

class CreateCompany(forms.ModelForm):
    """company form"""
    class Meta:
        """company form fields"""
        model = Company
        fields = ['company_name', 'company_employees', 'company_type', 'country']

class CreateProject(forms.ModelForm):
    """project form"""
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if hasattr(user, 'company') and user.company:
            self.fields['client'].queryset = Client.objects.filter(company = user.company).all()
        else:
            self.fields['client'].queryset = Client.objects.none()

    class Meta:
        """project form fields"""
        model = Project
        fields = ['client', 'project_name', 'project_deadline']
        widgets = {
        'project_deadline': forms.DateInput(attrs={'type': 'date'}),
        }

class CreateMember(forms.ModelForm):
    """member form"""
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if hasattr(user, 'company') and user.company:
            clients = user.company.clients.all()
            self.fields['project'].queryset = Project.objects.filter(client__in=clients)
        else:
            self.fields['project'].queryset = Project.objects.none()

    class Meta:
        """member form fields"""
        model = Member
        fields = ['member_name', 'member_email', 'member_role', 'project']

class MemberAuth(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class RegisterTime(forms.ModelForm):
    """register time form"""

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if user.groups.filter(name='Admin').exists() and hasattr(user, 'company'):
            clients = user.company.clients.all()
            self.fields['project'].queryset = Project.objects.filter(client__in=clients)
        elif user.groups.filter(name='Member').exists():
            member = Member.objects.get(member_email=user.email)
            print(member)
            self.fields['project'].queryset = Project.objects.filter(id=member.project_id)
        self.fields['project'].widget.attrs.update({'class': 'p-2 bg-gray-100 rounded-md'})

    class Meta:
        """register time form fields"""
        model = RegisterHours
        fields = ['project', 'date']
        widgets = {
        'date': forms.DateInput(attrs={'type': 'date', 'class': 'p-2 bg-gray-100 rounded-md'}),
        }
