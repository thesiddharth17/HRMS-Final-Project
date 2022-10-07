from django.db import models
import random
from django.urls import reverse
from django.utils import timezone
import time
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    thumb = models.ImageField()

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length=70, null=False, blank=False)
    history = models.TextField(max_length=1000,null=True,blank=True, default='No History')
    

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("hrms:dept_detail", kwargs={"pk": self.pk})
    

class Employee(models.Model):
    LANGUAGE = (('english','ENGLISH'),('yoruba','YORUBA'),('hausa','HAUSA'),('french','FRENCH'))
    GENDER = (('male','MALE'), ('female', 'FEMALE'),('other', 'OTHER'))
    emp_id = models.CharField(max_length=70, default='emp'+str(random.randrange(100,999,1)))
    thumb = models.ImageField(blank=True,null=True)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    mobile = models.CharField(max_length=15)
    email = models.EmailField(max_length=125, null=False)
    address = models.TextField(max_length=100, default='')
    emergency = models.CharField(max_length=11)
    gender = models.CharField(choices=GENDER, max_length=10)
    department = models.ForeignKey(Department,on_delete=models.SET_NULL, null=True)
    joined = models.DateTimeField(default=timezone.now)
    language = models.CharField(choices=LANGUAGE, max_length=10, default='english')
    account = models.CharField(max_length=10, default='0123456789')
    bank = models.CharField(max_length=25, default='First Bank Plc')
    salary = models.CharField(max_length=16,default='00,000.00')      
    def __str__(self):
        return self.first_name
        
    def get_absolute_url(self):
        return reverse("hrms:employee_view", kwargs={"pk": self.pk})
    

# class Kin(models.Model):
#     first_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=20)
#     address = models.TextField(max_length=100)
#     occupation = models.CharField(max_length=20)
#     mobile = models.CharField(max_length=15)
#     employee = models.OneToOneField(Employee,on_delete=models.CASCADE, blank=False, null=False)

#     def __str__(self):
#         return self.first_name+'-'+self.last_name
    
#     def get_absolute_url(self):
#         return reverse("hrms:employee_view",kwargs={'pk':self.employee.pk})
    

class Attendance (models.Model):
    STATUS = (('PRESENT', 'PRESENT'), ('ABSENT', 'ABSENT'),('UNAVAILABLE', 'UNAVAILABLE'))
    date = models.DateField(auto_now_add=True)
    first_in = models.TimeField()
    last_out = models.TimeField(null=True)
    status = models.CharField(choices=STATUS, max_length=15 )
    staff = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True)
    def save(self,*args, **kwargs):
        self.first_in = timezone.localtime()
        super(Attendance,self).save(*args, **kwargs)
    
    def __str__(self):
        return 'Attendance -> '+str(self.date) + ' -> ' + str(self.staff)

    def hrs_of_work(self):
        at_work=self.first_in-self.last_out
        return at_work



class breakdown (models.Model):
    position = models.CharField(max_length=100)
    basic_salary = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.position


class Payslip(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    working_days = models.PositiveIntegerField(default=0)
    number_of_days_present = models.PositiveIntegerField(default=0)
    job_position = models.ForeignKey(breakdown, on_delete=models.CASCADE)
    gross_salary = models.PositiveIntegerField(default=0)
    net_salary = models.PositiveIntegerField(default=0)
    csg = models.PositiveIntegerField(default=0)
    nsf = models.PositiveIntegerField(default=0)
    prgf = models.PositiveIntegerField(default=0)
    paye = models.PositiveIntegerField(default=0)

    # gross_salary = basic_salary * days

    def save(self, *args, **kwargs):
        
        self.gross_salary = int(self.employee.salary) / self.working_days*self.number_of_days_present

        self.csg= self.gross_salary * 0.035
        self.nsf= self.gross_salary * 0.035
        self.prgf= self.gross_salary * 0.045  
        self.net_salary = self.gross_salary - self.csg - self.nsf - self.prgf
        if self.gross_salary>= 25000:
            self.paye=self.gross_salary * 0.1

            self.net_salary = self.gross_salary - self.csg - self.nsf - self.prgf-self.paye
        return super().save(*args, **kwargs) 




    def __str__(self):
        return self.employee.first_name







class Leave (models.Model):
    STATUS = (('approved','APPROVED'),('unapproved','UNAPPROVED'),('decline','DECLINED'))
    employee = models.OneToOneField(Employee, on_delete=models.CASCADE)
    start = models.CharField(blank=False, max_length=15)
    end = models.CharField(blank=False, max_length=15)
    status = models.CharField(choices=STATUS,  default='Not Approved',max_length=15)

    def __str__(self):
        return self.employee + ' ' + self.start

class Recruitment(models.Model):
    first_name = models.CharField(max_length=25)
    last_name= models.CharField(max_length=25)
    position = models.CharField(max_length=15)
    email = models.EmailField(max_length=25)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.first_name +' - '+self.position


