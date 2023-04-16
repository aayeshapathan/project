from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.register, name='register'),
    path('u_register', views.u_register , name='u_register'),
    path('c_register', views.c_register , name='c_register'),
    path('Edudetails', views.Edudetails , name='Edudetails'),
    path('login', views.login , name='login'),
    path('jobdescription/<int:id>/', views.jobdescription , name='jobdescription'),
    path('jobdescription', views.jobdescription , name='jobdescription'),

    path('dataentry', views.dataentry , name='dataentry'),
    path('mobile', views.mobile , name='mobile'),
    path('content', views.content , name='content'),

    path('jobdescriptionform/<int:company_id>/', views.jobdescriptionform , name='jobdescriptionform'),
    path('jobdescriptionform', views.jobdescriptionform , name='jobdescriptionform'),

    path('description', views.description , name='description'),
    path('vacancy', views.vacancy , name='vacancy'),

    path('u_profilepage/<int:id>/', views.u_profilepage , name='u_profilepage'),
    path('u_profilepage', views.u_profilepage , name='u_profilepage'),

    path('u_profile/<int:uid>/', views.u_profile , name='u_profile'),
    path('u_profile', views.u_profile , name='u_profile'),
    path('user_profile', views.user_profile , name='user_profile'),

    path('c_profilepage', views.c_profilepage , name='c_profilepage'),

    path('u_Editform/<int:uid>/', views.u_Editform , name='u_Editform'),
    path('u_Editform', views.u_Editform , name='u_Editform'),
    
    path('search', views.search , name='search'),
    path('locationjob', views.locationjob , name='locationjob'),
    path('skillsjob', views.skillsjob , name='skillsjob'),
    path('freshersjob', views.freshersjob , name='freshersjob'),
    path('workfromhome', views.workfromhome , name='workfromhome'),
    path('companyjob', views.companyjob , name='companyjob'),
    path('androidjob', views.androidjob , name='androidjob'),
    path('dataentryjob', views.dataentryjob , name='dataentryjob'),
    path('accountantjob', views.accountantjob , name='accountantjob'),
    path('interiordesignerjob', views.interiordesignerjob , name='interiordesignerjob'),
    path('systemanalystjob', views.systemanalystjob , name='systemanalystjob'),
    path('businessanalystjob', views.businessanalystjob , name='businessanalystjob'),
    path('contentwriterjob', views.contentwriterjob , name='contentwriterjob'),
    path('othersjob', views.othersjob , name='othersjob'),
    path('aboutus', views.aboutus , name='aboutus'),
    path('interviewpage', views.interviewpage , name='interviewpage'),
    path('accounthome', views.accounthome , name='accounthome'),
    path('log', views.log , name='log'),

    path('apply', views.apply , name='apply'),
    path('apply/<int:j_id>/', views.apply , name='apply'),
    path('apply_now', views.apply_now , name='apply_now'),

    path('logout/<int:user_id>/', views.logout , name='logout'),
    path('logout', views.logout , name='logout'),

    path('companyprofile/<int:cid>/', views.companyprofile , name='companyprofile'),
    path('companyprofile', views.companyprofile , name='companyprofile'),
    
    path('viewdetails/<int:vid>/<int:aid>/', views.viewdetails , name='viewdetails'),
    path('viewdetails', views.viewdetails , name='viewdetails'),

    path('view', views.view , name='view'),

    path('selectlogin', views.selectlogin , name='selectlogin'),
    path('c_login', views.c_login , name='c_login'),

    path('VacancyDelete', views.VacancyDelete , name='VacancyDelete'),
    path('VacancyDelete/<int:jdelid>/', views.VacancyDelete , name='VacancyDelete'),

]

