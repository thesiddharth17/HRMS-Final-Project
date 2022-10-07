from django.contrib import admin
from .models import Employee,Department,Attendance,breakdown,Payslip
# Register your models here.

class FinalPay(admin.ModelAdmin):
    list_display = ( 'employee','working_days', 'number_of_days_present','job_position', 'gross_salary', 'net_salary')

admin.site.register([Employee,Department,Attendance,breakdown])
admin.site.register(Payslip, FinalPay)
