# Generated by Django 4.1 on 2022-10-07 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0007_rename_payslip_breakdown_alter_employee_emp_id'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Staff',
            new_name='Payslip',
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(default='emp307', max_length=70),
        ),
    ]