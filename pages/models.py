from django.db import models

# Create your models here.
#for _JobDescription in JobDescription.objects.all():
#    _JobDescription.learningobjective_set.all()

class User(models.Model):
    
    ID=models.IntegerField()
    FName=models.CharField(max_length=100)
    MName=models.CharField(max_length=100)
    LName=models.CharField(blank=False ,max_length=100)
    email=models.EmailField(max_length=100)
    pwd=models.CharField(max_length=100)
    Gender=models.CharField(max_length=10)
    MobileNumber=models.CharField(blank=False, max_length=10)
    Address=models.CharField(max_length=100)
    Education=models.CharField(max_length=100)
    Skills=models.TextField(max_length=100)
    Experience=models.IntegerField()
    Rfile=models.FileField(blank=True)
    U_login=models.BooleanField(default=False)

    class Meta:
        #managed = True
        db_table='User'

class Company(models.Model):
    
    ID=models.IntegerField()
    CName=models.CharField(max_length=100)
    CInfo=models.TextField(max_length=100)
    email=models.EmailField(max_length=100)
    pwd=models.CharField(max_length=100)
    Location=models.CharField(max_length=100)
    MobileNumber=models.IntegerField()
    RegistrationNo=models.CharField(max_length=100)
    C_login=models.BooleanField(default=False)

    class Meta:
        db_table='Company'  

    """def __unicode__(self):
        return self.CName """ 

class JobDescription(models.Model):
    
    ID=models.IntegerField()
    UKID=models.IntegerField()
    #CName=models.ForeignKey(Company)
    CName=models.CharField(max_length=100)
    CInfo=models.TextField(max_length=100)
    Location=models.CharField(max_length=100)
    Position=models.CharField(max_length=100)
    Description=models.TextField(max_length=100)
    JobType=models.CharField(max_length=100)
    Knowledge_Skills=models.TextField(max_length=100)
    Education=models.TextField(max_length=100)
    Experience=models.TextField(max_length=100)
    Salary=models.IntegerField()
    Vacancies=models.IntegerField()
    #Lastdate=models.DateField((""), auto_now=False, auto_now_add=False)
    Lastdate=models.DateField()
    #UKID=models.IntegerField()

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)  # get parent context
    #     # the model here should be replaced with the object that has the "tag" attribute. DO NOT use the "model" word.
    #     # Try self.object.tag.split(',')
    #     tag_list = self.Knowledge_Skills.split(',')  # conversion from a string to a list
    #     context['tag_list'] = tag_list  # add to the context the tag_list list
    #     return context
    def tags_list(self):
         return self.Knowledge_Skills.split(',')

    class Meta:
        db_table='Jobdescription'     

class Application(models.Model):
    
    ID=models.IntegerField()
    J_ID=models.IntegerField()
    C_ID=models.IntegerField()
    U_ID=models.IntegerField()
    Status=models.CharField(max_length=20)
    #J_ID=models.ForeignKey(JobDescription, on_delete=models.CASCADE)
    #U_ID=models.ForeignKey(User, on_delete=models.CASCADE)
    #Resume_file=models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table='application'
    

#python manage.py makemigrations
