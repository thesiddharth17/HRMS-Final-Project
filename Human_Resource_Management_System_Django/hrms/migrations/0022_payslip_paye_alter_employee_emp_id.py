# Generated by Django 4.1 on 2022-10-07 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms', '0021_alter_employee_emp_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='payslip',
            name='paye',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_id',
            field=models.CharField(default='emp623', max_length=70),
        ),
    ]