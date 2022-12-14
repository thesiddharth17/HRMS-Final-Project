# Generated by Django 4.1 on 2022-10-07 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0019_alter_employee_emp_id_alter_payslip_csg_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(default='emp725', max_length=70),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='csg',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='nsf',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='payslip',
            name='prgf',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
