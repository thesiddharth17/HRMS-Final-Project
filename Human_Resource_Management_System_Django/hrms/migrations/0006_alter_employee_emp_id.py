# Generated by Django 4.1 on 2022-10-07 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0005_payslip_staff_alter_employee_emp_id_delete_kin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(default='emp683', max_length=70),
        ),
    ]
