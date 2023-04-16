from django.shortcuts import render,redirect
from django.http import HttpResponse 
from pages.models import User
from pages.models import Company
from pages.models import JobDescription
from pages.models import Application
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.core.files.storage import FileSystemStorage
from django.core.mail import send_mail
from django.conf import settings


# Create your views here.
def home(request):
    #Jobs = JobDescription.objects.all()
    Jobs = JobDescription.objects.all().order_by('ID').reverse()[:3]
   # Jobs = get_object_or_404(JobDescription, pk=jobdescription_id)
    paginator = Paginator(Jobs,3)
    page = request.GET.get('page')
    #print(page)
    paged_Jobs = paginator.get_page(page)
    if 'user_id' in request.session:
        user_id = request.session['user_id']    
        context = {
            'Jobs': paged_Jobs,
            'user_id' : user_id
        }
    elif 'company_id' in request.session:
        company_id = request.session['company_id']    
        context = {
            'Jobs': paged_Jobs,
            'company_id' : company_id
        }
    else:    
        context = {
            'Jobs': paged_Jobs
        }

    return render(request, 'pages/home.html', context)

def register(request):
    return render(request, 'pages/register.html')

def selectlogin(request):
    return render(request, 'pages/selectlogin.html')

def aboutus(request):
    return render(request, 'pages/aboutus.html')

def interviewpage(request):
    return render(request, 'pages/interviewpage.html')

def u_register(request):
    print("true")
    if request.method == 'POST':
        if request.POST.get('pwd')==request.POST.get('pwd_confirm'):
            print("true")
            # if request.POST.get('FName') and request.POST.get('LName') and request.POST.get('email') and request.POST.get('pwd') and request.POST.get('Gender') and request.POST.get('MobileNumber') or request.POST.get('MName') or request.POST.get('Skills') or request.POST.get('Experience') or request.POST.get('Rfile'):
            print("true")
            saverecord=User()
            print(saverecord)
            saverecord.FName=request.POST.get('FName')
            print(saverecord.FName)
            if request.POST.get('MName'):
                saverecord.MName=request.POST.get('MName')
                print(saverecord.MName)
            saverecord.LName=request.POST.get('LName')
            print(saverecord.LName)
            saverecord.email=request.POST.get('email')
            print(saverecord.email)
            saverecord.pwd=request.POST.get('pwd')
            saverecord.Gender=request.POST.get('Gender')
            print(saverecord.Gender)
            saverecord.MobileNumber=request.POST.get('MobileNumber')
            print(saverecord.MobileNumber)
            saverecord.Address=request.POST.get('Address')
            print(saverecord.Address)
            saverecord.Education=request.POST.get('Education')
            print(saverecord.Education)
            if request.POST.get('Skills'):
                saverecord.Skills=request.POST.get('Skills')
            if request.POST.get('Experience'):
                saverecord.Experience=request.POST.get('Experience')
            #saverecord.Rfile=request.POST.get('Rfile')
            Rfile = request.FILES['Rfile']
            fs = FileSystemStorage()
            filename = fs.save(Rfile.name, Rfile)
            uploaded_file_url = fs.url(filename)
            print(uploaded_file_url)
            saverecord.Rfile = uploaded_file_url
            print(saverecord.Rfile)
            saverecord.save()    

            subject = 'Thank you for registering to our site'
            message = 'Thank you for registering on our website online job portal "SPARKLE". Now Just login and apply for your dream job with the best as location, position and skills!  '
            email_from = settings.EMAIL_HOST_USER
            recipient_list = ['sparklejobportal@gmail.com',]
            send_mail( subject, message, email_from, recipient_list )

            context = {
                        'valid': "Data submitted successfully."
            }  
            return render(request, 'pages/u_register.html', context)
        else:
            context = {
                'Invalid': "Password and Confirm password didn't match!"
            }
            return render(request, 'pages/u_register.html', context)

        
        """if request.method == 'POST' and request.FILES['myfile']:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            return render(request, 'core/simple_upload.html', {
                'uploaded_file_url': uploaded_file_url
            })
            return render(request, 'pages/u_register.html')
            """


    else:
        return render(request, 'pages/u_register.html')

def Edudetails(request):
    return render(request, 'pages/Edudetails.html')

def c_register(request):
    if request.method == 'POST':
        if request.POST.get('CName') and request.POST.get('email') and request.POST.get('pwd') and request.POST.get('MobileNumber') or request.POST.get('RegistrationNo'):
            if request.POST.get('pwd')==request.POST.get('pwd_confirm'):
                saverecord=Company()
                saverecord.CName=request.POST.get('CName')
                saverecord.CInfo=request.POST.get('CInfo')
                saverecord.email=request.POST.get('email')
                saverecord.pwd=request.POST.get('pwd')
                saverecord.Location=request.POST.get('Location')
                saverecord.MobileNumber=request.POST.get('MobileNumber')
                saverecord.RegistrationNo=request.POST.get('RegistrationNo')
                saverecord.save()  

                subject = 'Thank you for registering to our site'
                message = 'Thank you so much for registering on our website online job portal "SPARKLE". We would love, If you login to your account and then post and update job vacancies in your company for desired position with all necessary details required.'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = ['sparklejobportal@gmail.com',]
                send_mail( subject, message, email_from, recipient_list )

                context = {
                    'valid': "Data submitted successfully."
                }  
                return render(request, 'pages/c_register.html', context)
            else:
                context = {
                    'Invalid': "Password and Confirm password didn't match!"
                }
                return render(request, 'pages/c_register.html', context)
    else:
        return render(request, 'pages/c_register.html')
    

def login(request):
    print("true")
    #if request.method == 'POST':
        #print("true")
    if request.POST.get('email'):
        #saverecord=User()
        print("true")
        EmailCheck=request.POST.get('email')
        print(EmailCheck)
        #search3 = searchpage
        user = User.objects.filter(email=EmailCheck).first()
        
        print(user)
        if user:
            PswdCheck=request.POST.get('pwd')
            if user.pwd==PswdCheck:
                print(user.U_login)
                user.U_login = True
                print("Worked")
                request.session['user_id'] = user.ID
                print(request.session['user_id'])
                #saverecord.U_login = user.U_login
                User.objects.filter(ID=request.session['user_id']).update(U_login=True)
                print(user.U_login)
                #saverecord.save()
                return redirect('home')

            else:
                print("Email  or password didn't match!")

                context = {
                        'Invalid': "Email or password didn't match!"
                }
                return render(request, 'pages/login.html', context)
    else:
        return render(request, 'pages/login.html')

def c_login(request):
    print("true")
    #if request.method == 'POST':
        #print("true")
    if request.POST.get('email'):
        #saverecord=User()
        print("true")
        EmailCheck=request.POST.get('email')
        print(EmailCheck)
        #search3 = searchpage
        company = Company.objects.filter(email=EmailCheck).first()
        print(company)
        if company:
            PswdCheck=request.POST.get('pwd')
            if company.pwd==PswdCheck:
                print(company.C_login)
                company.C_login = True
                print("Worked")
                request.session['company_id'] = company.ID
                print(request.session['company_id'])
                #saverecord.U_login = user.U_login
                Company.objects.filter(ID=request.session['company_id']).update(C_login=True)
                print(company.C_login)
                #saverecord.save()
                return redirect('home')

            else:
                print("Email  or password didn't match!")

                context = {
                        'Invalid': "Email  or password didn't match!"
                }
                return render(request, 'pages/c_login.html', context)
    else:
        return render(request, 'pages/c_login.html')

#url(r'^/job-portal/pages/urls.py/(?P<Job_Description_ID>\d+)/$', jobdescription),


#def paginas(request, **kwargs):
    
#    page = get_object_or_404(Page, id=id)

def jobdescription(request,id):

    #id = kwargs.pop('Job_Description_ID')
    #Job_Description = get_object_or_404(JobDescription, id=id)
    #if request.method == 'POST':
        #if request.POST.get('job_id'):  
           # saverecord.job_id=request.POST.get('job_id')
     #      print(saverecord.job_id) 
    Job_Description = JobDescription.objects.filter(ID=id).first()
    k_s = Job_Description.Knowledge_Skills.split(',')
    experience = Job_Description.Experience.split(',')
    education = Job_Description.Education.split(',')
    
    print("\n\n\n",k_s)
    print("\n\n\n",education)
    print("\n\n\n",experience)
    print("\n\n\nJD: ",Job_Description)
    if 'user_id' in request.session:
        user_id = request.session['user_id']    
        context = {
            'Job_Description':Job_Description,
            'k_s' : k_s,
            'experience' : experience,
            'education' : education,
            'user_id' : user_id
        }
        return render(request, 'pages/jobdescription.html', context)
    context = {
        'k_s' : k_s,
        'experience' : experience,
        'education' : education,
        'Job_Description':Job_Description
    }
            
    return render(request, 'pages/jobdescription.html', context)

def dataentry(request):
    return render(request, 'pages/dataentry.html')

def mobile(request):
    return render(request, 'pages/mobile.html')

def content(request):
    return render(request, 'pages/content.html')

def jobdescriptionform(request, company_id):        
    
    """saverecord.UKID=company_id
    
    """
    Cuser = Company.objects.get(ID=company_id)
    print("\n\n\nJD: ",company_id)
    context = {
        'Cuser':Cuser
    }
    """        

    j_id = request.POST.get('jd_id')
    jobdescription = JobDescription.objects.filter(ID=j_id).first()
    saverecord.UKID=jobdescription.ID
    
    else:
return render(request, 'pages/jobdescriptionform.html')
    """
        
    
    return render(request, 'pages/jobdescriptionform.html', context)
    

def description(request):
    if request.method == 'POST':
        print("true")
        #if request.POST.get('CName') and request.POST.get('CInfo') and request.POST.get('Location') and request.POST.get('Position') and request.POST.get('Description') and request.POST.get('JobType') and request.POST.get('Knowledge_Skills') and request.POST.get('Education') and request.POST.get('Experience') and request.POST.get('Salary') and request.POST.get('Vacancies') and request.POST.get('Lastdate'):
        print("false")
        saverecord=JobDescription()
        saverecord.CName=request.POST.get('CName')
        print(saverecord.CName)
        saverecord.CInfo=request.POST.get('CInfo')
        saverecord.Location=request.POST.get('Location')
        saverecord.Position=request.POST.get('Position')
        saverecord.Description=request.POST.get('Description')
        saverecord.JobType=request.POST.get('JobType')
        saverecord.Knowledge_Skills=request.POST.get('Knowledge_Skills')
        saverecord.Education=request.POST.get('Education')
        saverecord.Experience=request.POST.get('Experience')
        saverecord.Salary=request.POST.get('Salary')
        saverecord.Vacancies=request.POST.get('Vacancies')
        saverecord.Lastdate=request.POST.get('Lastdate')
        #uk_id = 
        #jobdescription = JobDescription.objects.filter(UKID=uk_id).first()
        saverecord.UKID=request.POST.get('uk_id')
        saverecord.save()
        return render(request, 'pages/jobdescriptionform.html')
    else:
        return render(request, 'pages/jobdescriptionform.html')

def search(request):
    search3 = ''
    if request.method == 'POST':
        JobSearch = JobDescription.objects.all()

        searchpage=request.POST.get('searchpage')
        print(searchpage)
        search3 = searchpage
    JobSearch = JobDescription.objects.filter(Position__icontains=search3)
    paginator = Paginator(JobSearch,5)
    page = request.GET.get('page')
    #print(page)
    paged_JobSearch = paginator.get_page(page)
    context = {
           'JSearch':paged_JobSearch
    }
    #queryset_list = JobDescription.objects.order_by('Lastdate')
    #if 'Position' in request.GET:
        #Position = request.GET['Position']
       # if Position:
            #queryset_list = queryset_list.filter(Position__icontains=Position)
    
    return render(request, 'pages/search.html', context)
    #return render(request, 'pages/search.html')

def u_profilepage(request, id):
    JUser = User.objects.get(ID=id)
    context = {
        'JUser':JUser
    }
    return render(request, 'pages/u_profilepage.html', context)

def u_profile(request, uid):
    JUser = User.objects.get(ID=uid)
    applications = Application.objects.filter(U_ID=uid)

    l=[]
    #a=[]
    for app in applications:
        d=dict()
        user = JobDescription.objects.filter(ID=app.J_ID).first()
        d['Applied']=user
        job = Application.objects.filter(Status=app.Status).first()
        d['Status']=job
        #d['a']=app.ID
        l.append(d)

    context = {
        'JUser':JUser,
        'applications': applications,
        'l':l
    }
    return render(request, 'pages/u_profile.html', context)

def user_profile(request):
    FName=request.POST.get('FName')
    User.objects.filter(ID=request.session['user_id']).update(FName=FName)
    MName=request.POST.get('MName')
    User.objects.filter(ID=request.session['user_id']).update(MName=MName)
    LName=request.POST.get('LName')
    User.objects.filter(ID=request.session['user_id']).update(LName=LName)
    email=request.POST.get('email')
    User.objects.filter(ID=request.session['user_id']).update(email=email)
    MobileNumber=request.POST.get('MobileNumber')
    User.objects.filter(ID=request.session['user_id']).update(MobileNumber=MobileNumber)
    Address=request.POST.get('Address')
    User.objects.filter(ID=request.session['user_id']).update(Address=Address)
    Education=request.POST.get('Education')
    User.objects.filter(ID=request.session['user_id']).update(Education=Education)
    Experience=request.POST.get('Experience')
    User.objects.filter(ID=request.session['user_id']).update(Experience=Experience)
    Skills=request.POST.get('Skills')
    User.objects.filter(ID=request.session['user_id']).update(Skills=Skills)
    Rfile = request.FILES['Rfile']
    fs = FileSystemStorage()
    filename = fs.save(Rfile.name, Rfile)
    uploaded_file_url = fs.url(filename)
    print(uploaded_file_url)
    #Rfile=request.POST.get('Rfile')
    User.objects.filter(ID=request.session['user_id']).update(Rfile=uploaded_file_url)
    print("true")
    return render(request, 'pages/u_Editform.html')

def c_profilepage(request):
    # Job_Description = JobDescription.objects.get(pk=7)
    #Job_Description = JobDescription.objects.get(request.session['company_id'])
    #for j in Job_Description:
    #    print(j)
    # print(request.session['company_id'])
    # applications = Application.objects.get(C_ID=request.session['company_id'])
    # print(application.C_ID)
    # name= User.objects.get(ID=application.U_ID)
    # jd= JobDescription.objects.get(ID=application.J_ID)
    # #l=User.objects.filter(ID=)
    # print("SESSION : ",request.session['company_id'])
    application = Application.objects.filter(C_ID=request.session['company_id'])
    company = Company.objects.filter(ID=request.session['company_id']).first()
    l=[]
    a=[]
    for app in application:
        d=dict()
        user = User.objects.filter(ID=app.U_ID).first()
        d['User']=user
        job = JobDescription.objects.filter(ID=app.J_ID).first()
        d['Job']=job
        d['a']=app.ID
        l.append(d)
        #print(d['a'])
        #a.append(app.ID)
        print("App : ",l)
    #print(application)
    context = {
        'company':company,
        'l' : l,
        #'aplication':a
        # 'Job_Description':Job_Description,
        # 'application':application,
        # 'name':name,
        # 'jd':jd
    }
    return render(request, 'pages/c_profilepage.html', context)

def u_Editform(request, uid):

    JUser = User.objects.get(ID=uid)
    context = {
        'JUser':JUser
    }
    """User.objects.filter(ID=request.session['user_id']).update(email=request.GET.get('email'))
    print("true")
    User.objects.filter(ID=request.session['user_id']).update(MobileNumber=MobileNumber)
    User.objects.filter(ID=request.session['user_id']).update(Address=Address)
    User.objects.filter(ID=request.session['user_id']).update(Education=Education)
    User.objects.filter(ID=request.session['user_id']).update(Experience=Experience)
    User.objects.filter(ID=request.session['user_id']).update(Skills=Skills)
    User.objects.filter(ID=request.session['user_id']).update(Rfile=Rfile)"""

    return render(request, 'pages/u_Editform.html', context)

def locationjob(request):
    search3 = ''
    if request.method == 'POST':
        JobSearch = JobDescription.objects.all()

        searchpage=request.POST.get('locationpage')
        #print(searchpage)
        search3 = searchpage
    #print(search3)
    
    JobSearch = JobDescription.objects.filter(Location__icontains=search3)
    paginator = Paginator(JobSearch,5)
    page = request.GET.get('page')
    #print(page)
    paged_JobSearch = paginator.get_page(page)
    #print(paged_JobSearch)
    context = {
            'JSearch':paged_JobSearch
    }
    return render(request, 'pages/locationjob.html',{'JSearch':paged_JobSearch})
    # return render(request, 'pages/locationjob.html')


def skillsjob(request):
    search3 = ''
    if request.method == 'POST':
        JobSearch = JobDescription.objects.all()

        searchpage=request.POST.get('skillspage')
        print(searchpage)
        search3 = searchpage
    #print(search3)

    JobSearch = JobDescription.objects.filter(Knowledge_Skills__icontains=search3)
    paginator = Paginator(JobSearch,5)
    page = request.GET.get('page')
    #print(page)
    paged_JobSearch = paginator.get_page(page)

    context = {
            'JSearch':paged_JobSearch
    }
    return render(request, 'pages/skillsjob.html',{'JSearch':paged_JobSearch})
    #return render(request, 'pages/skillsjob.html')

def freshersjob(request):
    #if request.method == 'POST':
        #JobSearch = JobDescription.objects.all()

        #searchpage=request.POST.get('searchpage')
        #print(searchpage)
    JobSearch = JobDescription.objects.filter(Experience__icontains="0")
    paginator = Paginator(JobSearch,5)
    page = request.GET.get('page')
    #print(page)
    paged_JobSearch = paginator.get_page(page)

    context = {
            'JSearch':paged_JobSearch
    }
    return render(request, 'pages/freshersjob.html',context)
    #return render(request, 'pages/freshersjob.html')

def workfromhome(request):
    #if request.method == 'POST':
        #JobSearch = JobDescription.objects.all()

        #searchpage=request.POST.get('searchpage')
        #print(searchpage)
    JobSearch = JobDescription.objects.filter(JobType__icontains="Work From Home")
    paginator = Paginator(JobSearch,5)
    page = request.GET.get('page')
    #print(page)
    paged_JobSearch = paginator.get_page(page)

    context = {
            'JSearch':paged_JobSearch
    }
    return render(request, 'pages/workfromhome.html',context)
    #return render(request, 'pages/workfromhome.html')

def companyjob(request):
    search3 = ''
    if request.method == 'POST':
        JobSearch = JobDescription.objects.all()     

        searchpage=request.POST.get('companypage')
        print(searchpage)
        search3 = searchpage
    JobSearch = JobDescription.objects.filter(CName__icontains=search3)
    paginator = Paginator(JobSearch,5)
    page = request.GET.get('page')
    #print(page)
    paged_JobSearch = paginator.get_page(page)
    
    context = {
            'JSearch':paged_JobSearch
    }
    return render(request, 'pages/companyjob.html',context)
    #return render(request, 'pages/companyjob.html')

def androidjob(request):
    JobSearch = JobDescription.objects.filter(Position__icontains="android")
    paginator = Paginator(JobSearch,5)
    page = request.GET.get('page')
    #print(page)
    paged_JobSearch = paginator.get_page(page)

    context = {
            'JSearch':paged_JobSearch
    }
    return render(request, 'pages/androidjob.html',context)

def dataentryjob(request):
    JobSearch = JobDescription.objects.filter(Position__icontains="data entry")
    paginator = Paginator(JobSearch,5)
    page = request.GET.get('page')
    #print(page)
    paged_JobSearch = paginator.get_page(page)
    context = {
            'JSearch':paged_JobSearch
    }
    return render(request, 'pages/dataentryjob.html',context)

def accountantjob(request):
    JobSearch = JobDescription.objects.filter(Position__icontains="accountant")
    paginator = Paginator(JobSearch,5)
    page = request.GET.get('page')
    #print(page)
    paged_JobSearch = paginator.get_page(page)
    context = {
            'JSearch':paged_JobSearch
    }
    return render(request, 'pages/accountantjob.html',context)


def interiordesignerjob(request):
    JobSearch = JobDescription.objects.filter(Position__icontains="interior designer")
    paginator = Paginator(JobSearch,5)
    page = request.GET.get('page')
    #print(page)
    paged_JobSearch = paginator.get_page(page)
    context = {
            'JSearch':paged_JobSearch
    }
    return render(request, 'pages/interiordesignerjob.html',context)

def systemanalystjob(request):
    JobSearch = JobDescription.objects.filter(Position__icontains="system analyst")
    paginator = Paginator(JobSearch,5)
    page = request.GET.get('page')
    #print(page)
    paged_JobSearch = paginator.get_page(page)
    context = {
            'JSearch':paged_JobSearch
    }
    return render(request, 'pages/systemanalystjob.html',context)

def businessanalystjob(request):
    JobSearch = JobDescription.objects.filter(Position__icontains="business analyst")
    paginator = Paginator(JobSearch,5)
    page = request.GET.get('page')
    #print(page)
    paged_JobSearch = paginator.get_page(page)
    context = {
            'JSearch':paged_JobSearch
    }
    return render(request, 'pages/businessanalystjob.html',context)

def contentwriterjob(request):
    JobSearch = JobDescription.objects.filter(Position__icontains="content writer")
    paginator = Paginator(JobSearch,5)
    page = request.GET.get('page')
    #print(page)
    paged_JobSearch = paginator.get_page(page)
    context = {
            'JSearch':paged_JobSearch
    }
    return render(request, 'pages/contentwriterjob.html',context)

def othersjob(request):
    Jobs = JobDescription.objects.all()
    #JobSearch = JobDescription.objects.filter(Position__icontains="interior designer")
    paginator = Paginator(Jobs,5)
    page = request.GET.get('page')
    #print(page)
    paged_Jobs = paginator.get_page(page)

    context = {
            'Jobs':Jobs,
            'JSearch':paged_Jobs
    }
    return render(request, 'pages/othersjob.html',context)

def accounthome(request, id):
    Job_Description = JobDescription.objects.get(ID=id)
    print("\n\n\nJD: ",Job_Description)
    context = {
        'Job_Description':Job_Description
    }
    return render(request, 'pages/accounthome.html', content)

def log(request):
    return render(request, 'pages/log.html')


def logout(request, user_id):
    if 'user_id' in request.session:
        User.objects.filter(ID=request.session['user_id']).update(U_login=False)
        del request.session['user_id']
    else: 
        Company.objects.filter(ID=request.session['company_id']).update(C_login=False)
        del request.session['company_id']
    
    return redirect('home')


def apply(request, j_id):
#def apply(request, id, uid):
    """saverecord=Application()  
    saverecord.J_ID=id  
    saverecord.save()"""
    Job_Description = JobDescription.objects.get(ID=j_id)
    print("\n\n\nJD: ",Job_Description)
    JUser = User.objects.filter(ID=request.session['user_id']).first()
    context = {
        'Job_Description':Job_Description,
        'JUser':JUser
    }
    return render(request, 'pages/apply.html',context)

def apply_now(request):
     if request.method == 'POST':
        saverecord=Application()
        j_id = request.POST.get('jd_id')
        # print(j_id)
        # print("JID")
        jobdescription = JobDescription.objects.filter(ID=j_id).first()
        saverecord.J_ID=jobdescription.ID
        #jobdescription = JobDescription.objects.filter(ID=j_id).first()
        #saverecord.J_ID=jobdescription.ID
        saverecord.C_ID=jobdescription.UKID
        print(jobdescription.UKID)
        user_id = request.session['user_id']
        saverecord.U_ID=user_id
        print("Saved")
        saverecord.save()

        Education=request.POST.get('Education')
        User.objects.filter(ID=request.session['user_id']).update(Education=Education)
        Experience=request.POST.get('Experience')
        User.objects.filter(ID=request.session['user_id']).update(Experience=Experience)
        Skills=request.POST.get('Skills')
        User.objects.filter(ID=request.session['user_id']).update(Skills=Skills)
        Rfile = request.FILES['Rfile']
        fs = FileSystemStorage()
        filename = fs.save(Rfile.name, Rfile)
        uploaded_file_url = fs.url(filename)
        print(uploaded_file_url)
        #Rfile=request.POST.get('Rfile')
        User.objects.filter(ID=request.session['user_id']).update(Rfile=uploaded_file_url)

        return redirect('home')

def companyprofile(request, cid):
    CUser = Company.objects.get(ID=cid)
    context = {
        'CUser':CUser
    }
    return render(request, 'pages/companyprofile.html', context)        

def viewdetails(request, vid, aid):
    VUser = User.objects.get(ID=vid)
    AUser = Application.objects.get(ID=aid)
    context = {
        'VUser':VUser,
        'AUser':AUser
        #'aid':aid
    }
    return render(request, 'pages/viewdetails.html', context) 

def view(request):
    #if request.method == 'POST':
    #    if request.POST.get('status'): 
    print("true") 
    #        saverecord=Application()
            #print(request.POST.get('status'))
            #saverecord.Status=request.POST.get('status')
            #saverecord.save()
     #       return render(request, 'pages/view.html')
    AID=request.POST.get('a_id')
    status=request.POST.get('status')
    Application.objects.filter(ID=AID).update(Status=status)

    subject = 'Status of applied position'
    message = 'Please check your status from your account.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['sparklejobportal@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    
    return redirect('c_profilepage')

def vacancy(request):
    
    C=request.session['company_id']
    CUser= Company.objects.filter(ID=C).first()
    print(CUser)
    
    jobdescription = JobDescription.objects.filter(UKID=CUser.ID)
    print(jobdescription)
    
    context = {
        'CUser':CUser,
        'jobdescription':jobdescription
    }
    
    return render(request, 'pages/vacancy.html', context)
    
    #return render(request, 'pages/vacancy.html')

def VacancyDelete(request, jdelid):
    
    #JID=request.POST.get('j_id')
    #status=request.POST.get('status')
    #Application.objects.filter(J_ID=JID).update(Status=status)
    JobDescription.objects.filter(ID=jdelid).delete()
    return redirect('vacancy')