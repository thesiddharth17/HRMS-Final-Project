# Generated by Django 4.1 on 2022-10-07 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0012_alter_employee_emp_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payslip',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='payslip',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(default='emp903', max_length=70),
        ),
    ]