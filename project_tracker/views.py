"""imported modules"""
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.mail import send_mail
from django.contrib import messages
from .models import Company, Client, Project, Member, RegisterHours
from .forms import CreateClient, CreateCompany, CreateProject, CreateMember, MemberAuth, RegisterTime
from .decorators import allowed_users

def signin(request):
    """template for login"""
    form = AuthenticationForm()
    return render(request, "admin_login.html", {"form": form})

def register(request):
    """handling register template requests"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name = "Admin")
            user.groups.add(group)
            user.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, "admin_register.html", {"form": form})

def login_user(request):
    """handling login template requests"""
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                group = request.user.groups.all()[0].name
                if group == 'Member':
                    return redirect('track')
                elif group == 'Admin' and not Company.objects.filter(user=request.user).exists():
                    form = CreateCompany()
                    return render(request, "company.html", {"form":form})
                else:
                    myclients = Client.objects.filter(company=request.user.company).values()
                return render(request, "index.html", {"myclients":myclients, "username": username})
            else:
                return HttpResponse("Invalid Details")
    elif request.user.is_authenticated:
        myclients = Client.objects.filter(company=request.user.company).values()
        username = request.user.username
        return render(request, "index.html", {"myclients":myclients, "username": username})
    return redirect("login")

def logout_user(request):
    """handling logout template requests"""
    logout(request)
    return redirect('login')

def redirect_home(request):
    """handling home requests"""
    if request.user.is_authenticated and request.method == 'GET':
        return redirect('home')
    else:
        return redirect('login')

@allowed_users(allowed_roles=['Admin'])
def company(request):
    """handling company_details requests"""
    if request.method == 'POST':
        form = CreateCompany(request.POST)
        if request.user.is_authenticated:
            if form.is_valid():
                company_details = form.save(commit=False)
                company_details.user = request.user
                company_details.save()
                return redirect ("home")
        else:
            return HttpResponse("User is not authenticated.")
    return HttpResponse("You are not authorized to view this.")

@allowed_users(allowed_roles=['Admin'])
def add_client(request):
    """handling add_client requests"""
    if request.method == "POST":
        form = CreateClient(request.POST)
        if form.is_valid():
            client = form.save(commit=False)
            client.company = request.user.company
            client.save()
            messages.success(request, 'Client added successfully')
            return redirect("home")
    else:
        form = CreateClient()
    return render(request, 'add_client.html', {'form': form})

@allowed_users(allowed_roles=['Admin'])
def update_client(request, pk):
    """updating client info"""
    update = Client.objects.get(id=pk)
    form = CreateClient(request.POST, instance=update)
    if form.is_valid():
        form.save()
        messages.success(request, 'Client updated successfully')
        return redirect("home")
    return render(request, "edit_client.html", {"form":form})

@allowed_users(allowed_roles=['Admin'])
def delete_client(request, pk):
    """deleting client"""
    delete = Client.objects.get(id=pk)
    delete.delete()
    messages.success(request, 'Client deleted successfully')
    return redirect("home")

@allowed_users(allowed_roles=['Admin'])
def projects(request):
    """projects template"""
    clients = request.user.company.clients.all()
    myprojects = Project.objects.filter(client__in=clients)
    username = request.user.username
    return render(request, "projects.html", {"myprojects": myprojects, "username": username})

@allowed_users(allowed_roles=['Admin'])
def add_projects(request):
    """handling add_project requests"""
    if request.method == 'POST':
        form = CreateProject(request.user, request.POST)
        project = form.save(commit=False)
        if 'client' in form.cleaned_data:
            project.client = form.cleaned_data['client']
            project.save()
            messages.success(request, 'Project added successfully')
            return redirect("projects")
    else:
        form = CreateProject(request.user)
        myclients = Client.objects.filter(company=request.user.company).values()
    return render(request, "add_project.html", {"form":form, "myclients": myclients})

@allowed_users(allowed_roles=['Admin'])
def update_project(request, pk):
    """updating project info"""
    update = Project.objects.get(id=pk)
    form = CreateProject(request.user, request.POST, instance = update)
    if form.is_valid():
        project = form.save()
        if 'client' in form.cleaned_data:
            project.client = form.cleaned_data['client']
            messages.success(request, 'Project updated successfully')
            project.save()
    else:
        return render(request, "edit_project.html", {"form":form})
    return redirect("projects")

@allowed_users(allowed_roles=['Admin'])
def delete_project(request, pk):
    """deleting project"""
    delete = Project.objects.get(id=pk)
    delete.delete()
    messages.success(request, 'Project deleted successfully')
    return redirect("projects")

@allowed_users(allowed_roles=['Admin'])
def team(request):
    """team members template"""
    clients = request.user.company.clients.all()
    myprojects = Project.objects.filter(client__in=clients)
    mymembers = Member.objects.filter(project__in=myprojects)
    return render(request, "team_members.html", {"mymembers":mymembers})

@allowed_users(allowed_roles=['Admin'])
def add_team(request):
    """handling add_team requests"""
    if request.method == 'POST':
        form = CreateMember(request.user, request.POST)
        member = form.save(commit=False)
        member.project = form.cleaned_data['project']
        member.save()
        send_mail(
            "Welcome to Project Tracker",
            "",
            "Project Tracker",
            [f"{form.cleaned_data['member_email']}"],
            fail_silently=False,
            html_message=f"<p>Hi,</p><p>You have been invited to join {request.user.company} at Project Tracker.</p>"
                        f"<p>To sign in, first follow the link and setup your accout.</p>"
                        f"<p><a href='http://127.0.0.1:8000/memberlogin/'>Set your account</a></p>"
        )
        messages.success(request, 'Team member added successfully')
        return redirect("team")

    else:
        form = CreateMember(request.user)
        clients = request.user.company.clients.all()
        myprojects = Project.objects.filter(client__in=clients)
    return render(request, "add_member.html", {"form":form, "myprojects":myprojects})

def member_login(request):
    """handling register template requests"""
    if request.method == 'POST':
        form = MemberAuth(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name = "Member")
            user.groups.add(group)
            user.save()
            return redirect('login')
    else:
        form = MemberAuth()
    return render(request, "member_login.html", {"form": form})

@allowed_users(allowed_roles=['Admin', 'Member'])
def track(request):
    """handling timesheet requests"""
    group = request.user.groups.all()[0].name
    mytimesheet = RegisterHours.objects.filter(user=request.user)
    if request.method == 'POST':
        form = RegisterTime(request.user, request.POST)
        hours = int(request.POST.get('hours', 0))
        minutes = int(request.POST.get('minutes', 0))
        minutes_total = f"{hours} hours {minutes} minutes"
        time = form.save(commit=False)
        if 'project' in form.cleaned_data:
            time.project = form.cleaned_data['project']
            time.user = request.user
            time.time_spent = minutes_total
            messages.success(request, 'Entry added successfully')
            time.save()
    else:
        form = RegisterTime(request.user)
    return render(request, "track_hours.html", {"form": form, 'mytimesheet': mytimesheet, 'group': group})

@allowed_users(allowed_roles=['Admin', 'Member'])
def delete_track(request, pk):
    """deleting timesheet"""
    delete = RegisterHours.objects.get(id=pk)
    delete.delete()
    messages.success(request, 'Entry deleted successfully')
    return redirect("track")
