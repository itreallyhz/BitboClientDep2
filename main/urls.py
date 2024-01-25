from django.contrib import admin
from django.urls import path
from main import views
from .views import login

urlpatterns = [
    path('', views.login),
    path('login/', views.login, name='login'),
    path('SignUp/', views.SignUp, name='SignUp'),
    path('services/', views.services, name='services'),
    # path('navbar/', views.navbar, name='navbar'),
    # path('navbar_index/', views.navbar_index, name='navbar_index'),
    path('profiles/', views.profiles, name='profiles'),
    path('officials/', views.officials, name='officials'),
    path('forms/', views.forms, name='forms'),
    path('brgy_officials/', views.brgy_officials, name='brgy_officials'),
    path('projects/', views.projects, name='projects'),
    path('admin_forms/', views.admin_forms, name='admin_forms'),
    path('gov_admin/', views.gov_admin, name='gov_admin'),
    path('incident_logs/', views.incident_logs, name='incident_logs'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('doc_management/', views.doc_management, name='doc_management'),
    path('clearance_permit/', views.clearance_permit, name='clearance_permit'),
    path('faqs/', views.faqs, name='faqs'),
    path('terms_conditions/', views.terms_conditions, name='terms_conditions'),
    path('signup2/', views.signup2, name='signup2'),
    path('system_config/', views.system_config, name='system_config'),
    path('view_proj/', views.view_proj, name='view_proj'),
    path('view_gov/', views.view_gov, name='view_gov'),
    path('personnel_forms/', views.personnel_forms, name='personnel_forms'),
     path('personnel/', views.personnel, name='personnel'),
    path('add_incident/', views.add_incident, name='add_incident'),
    
    path('add_clearances/', views.add_clearances, name='add_clearances'),
    
 #userside
 
    path('user_login/', views.user_login, name='user_login'),
    path('user_index/', views.user_index, name='user_index'),
    path('user_proj_prog/', views.user_proj_prog, name='user_proj_prog'),
    path('user_home/', views.user_home, name='user_home'),
    path('user_profiles/', views.user_profiles, name='user_profiles'),
    path('user_officials/', views.user_officials, name='user_officials'),
    path('user_governance/', views.user_governance, name='user_governance'),
    path('user_clearance/', views.user_clearance, name='user_clearance'),
    path('user_doc_management/', views.user_doc_management, name='user_doc_management'),
    

    
    
    






#backend
    path('get-all-residents/', views.GetAllResidents),
    path('create-new-resident/', views.CreateNewResident),
    path('delete-resident/', views.DeleteResident),
    path('get-resident/', views.GetResident),
    path('update-resident/', views.UpdateResident),

]