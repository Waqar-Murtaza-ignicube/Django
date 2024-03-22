"""imported modules"""
from django.urls import path
from . import views

urlpatterns = [
    path("register/", views.register, name='register'),
    path("", views.redirect_home, name='root'),
    path("login/", views.signin, name='login'), 
    path("logout/", views.logout_user, name='logout'),

    path("home/", views.login_user, name='home'),
    path("home/company_details/", views.company, name='company'),

    path("home/add_client/", views.add_client, name='add_client'),
    path("home/add_client/create/", views.add_client, name='create'),
    path("home/delete_client/<int:pk>", views.delete_client, name='delete_client'),
    path("home/update_client/<int:pk>", views.update_client, name='update_client'),

    path("projects/", views.projects, name='projects'),
    path("projects/add_project/", views.add_projects, name='create_projects'),
    path("projects/add_project/create/", views.add_projects, name='create_projects'),
    path("projects/update_project/<int:pk>", views.update_project, name='update_project'),
    path("projects/delete_project/<int:pk>", views.delete_project, name='delete_project'),

    path("team/", views.team, name='team'),
    path("team/add_member/", views.add_team, name='create_team'),
    path("team/add_member/create/", views.add_team, name='create_team'),
    path("memberlogin/", views.member_login, name='memberlogin'),

    path("track/", views.track, name='track'),
    path("delete_track/<int:pk>", views.delete_track, name='delete_track'),
]
